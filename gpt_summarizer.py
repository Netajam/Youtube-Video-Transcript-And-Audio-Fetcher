import openai
import os
import glob
import aiohttp
import asyncio
from dotenv import load_dotenv
import time
from config import TRANSCRIPT_PARTS_DIR, GPT_SUMMARIES_COMBINED_DIR, GPT_SUMMARIES_PARTS_DIR, OPENAI_MODEL, TEMPLATES_DIR, SUMMARY_TEMPLATE_FILE, SUMMARY_FILES_DIR ,CHARACTER_PER_TOKEN
from file_utils import MarkdownWriter 
from constant import MODEL_TOKEN_LIMITS

class GPTSummarizer:
    def __init__(self, api_key, model=OPENAI_MODEL, prompt_folder=TRANSCRIPT_PARTS_DIR, output_folder_parts=GPT_SUMMARIES_PARTS_DIR, output_folder_combined=GPT_SUMMARIES_COMBINED_DIR, character_per_token=CHARACTER_PER_TOKEN):
        self.api_key = api_key
        self.model = model
        self.prompt_folder = prompt_folder
        self.output_folder_parts = output_folder_parts
        self.output_folder_combined = output_folder_combined
        self.responses = []
        self._character_per_token = character_per_token
        self.token_limit_per_minute = self.get_token_limit()
        self.token_count = 0
        self.start_time = time.time()
        self.lock = asyncio.Lock()
        self.markdown_writer = MarkdownWriter()
    
    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, new_api_key):
        self._api_key = new_api_key
        openai.api_key = new_api_key
    
    def get_token_limit(self):
        return MODEL_TOKEN_LIMITS.get(self.model, 30000)
    
    def count_tokens(self, prompt):
        return len(prompt) // self._character_per_token

    async def reserve_tokens(self, token_count):
        async with self.lock:
            while True:
                elapsed_time = time.time() - self.start_time
                # If 60 seconds have passed, reset the token count and timer
                if elapsed_time >= 60:
                    self.start_time = time.time()
                    self.token_count = 0
                
                # If we have enough available tokens, reserve them and proceed
                if self.token_count + token_count <= self.token_limit_per_minute:
                    self.token_count += token_count
                    print(f"Reserved {token_count} tokens, total: {self.token_count}")
                    return
                else:
                    # Wait for the remaining time in the minute before retrying
                    sleep_time = 60 - elapsed_time
                    print(f"Token limit reached, waiting {sleep_time} seconds...")
                    await asyncio.sleep(sleep_time)

    async def send_prompt(self, session, prompt):
        # Function to send prompt asynchronously to OpenAI and return the response
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
        
        token_count = self.count_tokens(prompt)
        
        # Reserve tokens before sending the request
        await self.reserve_tokens(token_count)

        try:
            async with session.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["choices"][0]["message"]["content"]
                else:
                    return f"Error {response.status}: {await response.text()}"
        except Exception as e:
            return f"Error while sending prompt: {e}"

    async def save_to_markdown(self, response, filename):
        # Function to save the response to a markdown file asynchronously
        if not os.path.exists(self.output_folder_combined):
            os.makedirs(self.output_folder_combined)
        try:
            output_file = os.path.join(self.output_folder_parts, filename)
            with open(output_file,"w", encoding='utf-8') as md_file:
                md_file.write(f"{response}\n")
            print(f"Markdown file '{output_file}' created successfully.")
        except Exception as e:
            print(f"Error while saving to markdown: {e}")

    async def save_combined_summary(self, filename):
        # Ensure the output_folder_combined exists
        if not os.path.exists(self.output_folder_combined):
            os.makedirs(self.output_folder_combined)
        # Save all the responses to a combined summary file in the correct order
        summary_filename=f"{self.output_folder_combined}/SM-GPT-{filename}.md"
        SUMMARY_TEMPLATE_FILE=f"{SUMMARY_FILES_DIR}/VD-SM-{filename}.md"
        self.markdown_writer.write_content_to_file(SUMMARY_TEMPLATE_FILE,summary_filename)
        try:
            with open(summary_filename, "w",  encoding='utf-8') as combined_file:
                for response in self.responses:
                    combined_file.write(f"{response}\n\n")
            print(f"All responses saved to combined summary file:summary_filename")
        except Exception as e:
            print(f"Error while saving combined summary: {e}")

    async def process_prompt_file(self, session, prompt_file, index):
        # Process each prompt file: send the prompt and save the response
        with open(prompt_file, "r") as file:
            prompt = file.read()
            print(f"Processing prompt from {prompt_file}...")

            # Send the prompt asynchronously
            response = await self.send_prompt(session, prompt)

            # Save the response to an individual markdown file
            output_filename = os.path.basename(prompt_file).replace(".md", "_R.md")
            await self.save_to_markdown(response, output_filename)

            # Store the response in the correct index for the combined summary
            self.responses[index] = response

    async def process_prompt_files(self,video_title):
        # Function to process all markdown prompt files concurrently and in order
        if not os.path.exists(self.output_folder_parts):
            os.makedirs(self.output_folder_parts)

        prompt_files = glob.glob(os.path.join(self.prompt_folder, "*.md"))
        self.responses = [None] * len(prompt_files)  # Pre-allocate a list to store responses in order
        
        async with aiohttp.ClientSession() as session:
            # Create a list of tasks for each file, along with its index
            tasks = [self.process_prompt_file(session, prompt_file, index) for index, prompt_file in enumerate(prompt_files)]
            
            # Run all tasks concurrently
            await asyncio.gather(*tasks)

        # Once all prompts are processed, save the combined summary
        await self.save_combined_summary(video_title)

# Example usage:
if __name__ == "__main__":
    load_dotenv(override=True)
    api_key = os.environ.get("OPENAI_API_KEY")
    print(api_key)  # You can set your API key as an environment variable
    summarizer = GPTSummarizer(api_key)
    
    # Process all the markdown prompt files
    asyncio.run(summarizer.process_prompt_files())

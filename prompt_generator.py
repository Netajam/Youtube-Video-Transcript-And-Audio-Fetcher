
from dotenv import load_dotenv
import os
import re
from googleapiclient.discovery import build
from video_details_fetcher import YouTubeVideoProcessor
import re
from transcript_fetcher import TranscriptFetcher

class PromptGenerator:
    def __init__(self, character_limit):
        self.character_limit = character_limit

    def parse_transcript_with_timestamps(self, transcript_text):
        """
        Parse raw transcript text with timestamps into a structured format:
        [{"timestamp": "HH:MM:SS", "text": "transcript text"}]
        """
        pattern = r'\[(\d{2}:\d{2}:\d{2})\](.*?)(?=\[\d{2}:\d{2}:\d{2}\]|$)'
        matches = re.findall(pattern, transcript_text, re.DOTALL)

        parsed_transcript = []
        for match in matches:
            timestamp, text = match
            parsed_transcript.append({'timestamp': timestamp.strip(), 'text': text.strip()})

        return parsed_transcript

    def convert_timestamp_to_seconds(self, timestamp):
        """Convert timestamp from HH:MM:SS or MM:SS format to total seconds for easier comparison."""
        parts = list(map(int, timestamp.split(':')))
        if len(parts) == 2:  # Format is MM:SS
            m, s = parts
            return m * 60 + s
        elif len(parts) == 3:  # Format is HH:MM:SS
            h, m, s = parts
            return h * 3600 + m * 60 + s

    def extract_timestamp_from_chapter(self, chapter):
        """
        Extract the timestamp from the chapter string.
        The chapter might be in the format '00:05:00 - Introduction' or '00 - Introduction',
        so we extract the timestamp part (HH:MM:SS or MM:SS).
        """
        # Use regex to find valid timestamps in the chapter string
        match = re.search(r'(\d{1,2}:\d{2}:\d{2}|\d{1,2}:\d{2})', chapter)
        if match:
            return match.group(0)
        return None

    def get_chapters_for_part(self, start_timestamp, end_timestamp, chapters):
        """
        Get chapters whose timestamps fall between the start and end timestamp of the transcript part.
        """
        start_seconds = self.convert_timestamp_to_seconds(start_timestamp)
        end_seconds = self.convert_timestamp_to_seconds(end_timestamp)

        relevant_chapters = []
        for chapter in chapters:
            chapter_timestamp = self.extract_timestamp_from_chapter(chapter)
            if chapter_timestamp:
                chapter_seconds = self.convert_timestamp_to_seconds(chapter_timestamp)
                if start_seconds <= chapter_seconds <= end_seconds:
                    relevant_chapters.append(chapter)

        return relevant_chapters

    def split_by_chapters_or_limit(self, transcript_with_timestamps, chapters=None):
        """
        Split transcript by chapters if they exist and respect the character limit.
        If no chapters, split directly by character limit.
        Returns:
        - A list of (chapters, transcript part) tuples, where each tuple contains the chapters associated with the part and the transcript part itself.
        """
        if chapters:
            return self.split_transcript_by_chapters(transcript_with_timestamps, chapters)
        else:
            return self.split_transcript_by_character_limit(transcript_with_timestamps)
    
    def split_transcript_by_chapters(self, transcript_with_timestamps, chapters):
        """
        Split transcript into parts based on chapters and character limit. 
        Track chapters that appear within the start and end timestamps of each part.
        """
        chapter_transcripts = []
        current_transcript_part = ""
        current_char_count = 0
        part_start_timestamp = None  # Track the start timestamp for each part

        for idx, entry in enumerate(transcript_with_timestamps):
            timestamp, text = entry['timestamp'], entry['text']
            text_with_timestamp = f"[{timestamp}] {text}"

            # Set the start timestamp for this part if it's not set
            if part_start_timestamp is None:
                part_start_timestamp = timestamp

            # If adding this text exceeds the character limit, store the current part and reset
            if current_char_count + len(text_with_timestamp) > self.character_limit:
                # Get the chapters associated with this part
                part_end_timestamp = transcript_with_timestamps[idx - 1]['timestamp']  # The last timestamp of this part
                relevant_chapters = self.get_chapters_for_part(part_start_timestamp, part_end_timestamp, chapters)

                # Append the relevant chapters and transcript part
                chapter_transcripts.append((relevant_chapters, current_transcript_part.strip()))

                # Reset the variables for the new part
                current_transcript_part = ""
                current_char_count = 0
                part_start_timestamp = timestamp  # Reset the start timestamp for the new part

            # Add the text to the current transcript part
            current_transcript_part += text_with_timestamp + " "
            current_char_count += len(text_with_timestamp)

        # Append the last part with its chapters
        if current_transcript_part:
            part_end_timestamp = transcript_with_timestamps[-1]['timestamp']
            relevant_chapters = self.get_chapters_for_part(part_start_timestamp, part_end_timestamp, chapters)
            chapter_transcripts.append((relevant_chapters, current_transcript_part.strip()))

        return chapter_transcripts

    def split_transcript_by_character_limit(self, transcript_with_timestamps):
        """
        Split the transcript solely based on character limit without chapters.
        Return:
        - A list of ([], transcript part) tuples.
        """
        transcript_parts = []
        current_transcript_part = ""
        current_char_count = 0

        for entry in transcript_with_timestamps:
            timestamp, text = entry['timestamp'], entry['text']
            text_with_timestamp = f"[{timestamp}] {text}"

            if current_char_count + len(text_with_timestamp) > self.character_limit:
                transcript_parts.append(([], current_transcript_part.strip()))  # No chapters
                current_transcript_part = ""
                current_char_count = 0

            current_transcript_part += text_with_timestamp + " "
            current_char_count += len(text_with_timestamp)

        if current_transcript_part:
            transcript_parts.append(([], current_transcript_part.strip()))  # No chapters

        return transcript_parts

    def generate_markdown_files(self, transcript_parts_with_chapters, output_dir="transcript_prompts"):
        """
        Generate a markdown file for each part of the transcript with prompt instructions, chapters, and transcript text.
        The transcript_parts_with_chapters is a list of tuples: (chapters, transcript_part).
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for idx, (chapters, part) in enumerate(transcript_parts_with_chapters):
            filename = os.path.join(output_dir, f"transcript_part_{idx + 1}.md")

            with open(filename, 'w') as file:
                file.write("## Prompt Instruction\n")
                file.write("Please summarize the following parts of this transcript:\n\n")

                file.write("## Chapters Included\n")
                if chapters:
                    included_chapters = ', '.join(chapters)
                    file.write(f"{included_chapters}\n\n")
                else:
                    file.write("No chapters available for this part.\n\n")

                file.write("## Transcript\n")
                file.write(part)

            print(f"Markdown file generated: {filename}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    from googleapiclient.discovery import build

    load_dotenv()

    # 1. Set up the YouTube API client
    api_key = os.getenv("youtube_api_key")
    youtube = build('youtube', 'v3', developerKey=api_key)

    # 2. Define the video ID
    video_id = 'naed4C4hfAg'

    # 3. Fetch the raw transcript with timestamps using the original function
    transcript_fetcher=TranscriptFetcher(video_id, youtube)
    raw_transcript = transcript_fetcher.get_video_transcript(video_id, include_timestamps=True)
    print("Raw transcript with timestamps:", raw_transcript)

    # 4. Create an instance of the PromptGenerator
    prompt_generator = PromptGenerator(character_limit=32000)

    # 5. Parse the raw transcript into structured format
    transcript_with_timestamps = prompt_generator.parse_transcript_with_timestamps(raw_transcript)
    print("Parsed transcript:", transcript_with_timestamps)

    # 6. Fetch chapters (for simplicity, we simulate this here)
    processor = YouTubeVideoProcessor(video_id, youtube)
    chapters = processor.extract_chapters_from_description()

    # 7. Split transcript based on chapters or character limit
    transcript_parts_with_chapters = prompt_generator.split_by_chapters_or_limit(transcript_with_timestamps, chapters)
    print(f"\nGenerated {len(transcript_parts_with_chapters)} parts of transcript.")

    # 8. Generate markdown files for each transcript part
    prompt_generator.generate_markdown_files(transcript_parts_with_chapters)
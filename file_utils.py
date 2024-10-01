import os
import re
from config import TRANSCRIPT_FILES_PATH, SUMMARY_FILES_PATH, TEMPLATES_PATH, TRANSCRIPT_TEMPLATE_FILE, SUMMARY_TEMPLATE_FILE

class MarkdownWriter:
    
    def write_content_to_file(self, content, destination_file_path):
        directory = os.path.dirname(destination_file_path)
        os.makedirs(directory, exist_ok=True)
        with open(destination_file_path, 'w', encoding='utf-8') as dest_file:
            dest_file.write(content)
        print(f"Content written to {destination_file_path}")
    # Function to write content to a markdown file
    def write_to_md(self, directory, filename, content):
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(content)
        return file_path

    # Function to load and fill a template
    def fill_template(self, template_name, **kwargs):
        template_path = os.path.join(TEMPLATES_PATH, template_name)
        template_content = self.read_template(template_path)
        return template_content.format(**kwargs)

    # Function to read a template file
    def read_template(self, template_path):
        with open(template_path, 'r', encoding='utf-8') as template_file:
            return template_file.read()

    # Function to sanitize a filename
    def sanitize_filename(self, title):
        sanitized_title = re.sub(r'[<>:"/\\|?*]', '', title)
        sanitized_title = re.sub(r'\s+', ' ', sanitized_title)
        return sanitized_title.strip()

    # Function to save a transcript to markdown
    def format_save_transcript(self, video_id, transcript, title, include_timestamps=False):
        filename, filled_template = self.format_transcript(video_id, transcript, title, include_timestamps)
        
        file_path = self.write_to_md(TRANSCRIPT_FILES_PATH, filename, filled_template)
        print(f"Transcript saved to {file_path}.")

    def format_transcript(self, video_id, transcript, title, include_timestamps):
        sanitized_title = self.sanitize_filename(title)
        filename = f"Tr-{sanitized_title}.md"
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        if not include_timestamps:
            transcript = transcript.replace('\n', ' ')

        filled_template = self.fill_template(
            TRANSCRIPT_TEMPLATE_FILE,
            title=sanitized_title,
            video_url=video_url,
            transcript=transcript
        )
        
        return filename,filled_template

    # Create  a summary markdown
    def format_save_summary(self, video_id, title):
        filename, filled_template = self.format_summary(video_id, title)
        
        file_path = self.write_to_md(SUMMARY_FILES_PATH, filename, filled_template)
        print(f"Video link summary saved to {file_path}.")

    def format_summary(self, video_id, title):
        sanitized_title = self.sanitize_filename(title)
        filename = f"VD-SM-{sanitized_title}.md"
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        filled_template = self.fill_template(
            SUMMARY_TEMPLATE_FILE,
            title=title,
            video_url=video_url
        )
        
        return filename,filled_template

if __name__ == "__main__":
    # Initialize the markdown writer with the templates path
    markdown_writer = MarkdownWriter(TEMPLATES_PATH)
    
    # Example of saving a transcript
    video_id = "abcd1234"
    transcript = "This is an example transcript for the video."
    title = "Example Video Title"
    markdown_writer.format_save_transcript(video_id, transcript, title, include_timestamps=True)
    
    # Example of saving a video link summary
    title = "Another Example Video"
    markdown_writer.format_save_summary(video_id, title)

import os
import re
from config import transcript_files_path, summary_files_path, templates_path, transcript_template_file, summary_template_file

class MarkdownWriter:
    
    def write_content_to_file(self, content, destination_file_path):
        directory = os.path.dirname(destination_file_path)
        os.makedirs(directory, exist_ok=True)
        with open(destination_file_path, 'w', encoding='utf-8') as dest_file:
            dest_file.write(content)
        print(f"Content written to {destination_file_path}")
    # Function to write content to a markdown file
    def write_to_file(self, directory, filename, content):
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(content)
        return file_path

    # Function to load and fill a template
    def fill_template(self, template_name, **kwargs):
        template_path = os.path.join(templates_path, template_name)
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
    def save_transcript_to_markdown(self, video_id, transcript, title, include_timestamps=False):
        sanitized_title = self.sanitize_filename(title)
        filename = f"Tr-{sanitized_title}.md"
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        if not include_timestamps:
            transcript = transcript.replace('\n', ' ')

        filled_template = self.fill_template(
            transcript_template_file,
            title=sanitized_title,
            video_url=video_url,
            transcript=transcript
        )
        
        file_path = self.write_to_file(transcript_files_path, filename, filled_template)
        print(f"Transcript saved to {file_path}.")

    # Function to save video link summary to markdown
    def save_video_link_to_markdown(self, video_id, title):
        sanitized_title = self.sanitize_filename(title)
        filename = f"VD-SM-{sanitized_title}.md"
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        filled_template = self.fill_template(
            summary_template_file,
            title=title,
            video_url=video_url
        )
        
        file_path = self.write_to_file(summary_files_path, filename, filled_template)
        print(f"Video link summary saved to {file_path}.")

if __name__ == "__main__":
    # Initialize the markdown writer with the templates path
    markdown_writer = MarkdownWriter(templates_path)
    
    # Example of saving a transcript
    video_id = "abcd1234"
    transcript = "This is an example transcript for the video."
    title = "Example Video Title"
    markdown_writer.save_transcript_to_markdown(video_id, transcript, title, include_timestamps=True)
    
    # Example of saving a video link summary
    title = "Another Example Video"
    markdown_writer.save_video_link_to_markdown(video_id, title)

import os
import re
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from file_utils import MarkdownWriter
from dotenv import load_dotenv
from config import TEMPLATES_PATH


class VideoProcessor:
    
    def __init__(self, video_id, youtube_client):
        self.video_id = video_id
        self.youtube = youtube_client
        self.video_details = None
        self.markdown_writer=MarkdownWriter()
        
    def fetch_video_details(self):
        """Fetches video details including the title, description, and other snippet info"""
        response = self.youtube.videos().list(id=self.video_id, part='snippet').execute()
        if 'items' in response and len(response['items']) > 0:
            self.video_details = response['items'][0]['snippet']
        else:
            raise ValueError(f"No video found with ID {self.video_id}")

    def get_video_description(self):
        """Returns the description of the video"""
        if not self.video_details:
            self.fetch_video_details()
        return self.video_details.get('description', '')

    def get_video_title(self):
        """Returns the title of the video"""
        if not self.video_details:
            self.fetch_video_details()
        return self.video_details.get('title', '')

    def get_chapters(self):
        """Tries to extract chapters from the video description if timestamps are present"""
        description = self.get_video_description()
        # Look for timestamps in the format HH:MM:SS or MM:SS
        timestamp_pattern = r'((\d{1,2}:\d{2}(:\d{2})?)\s+-\s+[^\n]+)'
        matches = re.findall(timestamp_pattern, description)
        
        if matches:
            chapters = []
            for match in matches:
                chapters.append(match[0])  # Each match is a tuple, the first element is the full match
            return chapters
        return None

    def process_transcript(self, include_timestamps=False):
        """Fetches and saves the transcript of the video"""
        transcript = self.get_video_transcript(include_timestamps)
        if transcript != 'Transcript not available':
            title = self.get_video_title()
            self.markdown_writer.format_save_transcript(self.video_id, transcript, title, include_timestamps)
            self.markdown_writer.format_save_summary(self.video_id, title)
        else:
            print(f"Unable to fetch transcript for video ID {self.video_id}.")

    def get_video_transcript(self, include_timestamps=False):
        """Fetches the transcript for the video if available"""
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)
            transcript = transcript_list.find_transcript(['en']).fetch()
            if include_timestamps:
                transcript_text = '\n'.join([f"[{self.format_timestamp(item['start'])}] {item['text']}" for item in transcript])
            else:
                transcript_text = ' '.join([item['text'] for item in transcript])
            return transcript_text
        except (TranscriptsDisabled, NoTranscriptFound):
            return 'Transcript not available'

    @staticmethod
    def format_timestamp(seconds):
        """Formats timestamps from seconds to HH:MM:SS format"""
        return f"{int(seconds // 3600):02d}:{int((seconds % 3600) // 60):02d}:{int(seconds % 60):02d}"


# Main execution block
if __name__ == "__main__":

# Set up YouTube API client
    load_dotenv()

    api_key = os.getenv("youtube_api_key")
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_id = 'naed4C4hfAg'

    processor = VideoProcessor(video_id, youtube)

    # Fetch video description
    description = processor.get_video_description()
    print("Video Description:", description)

    # Extract and print video chapters
    chapters = processor.get_chapters()
    if chapters:
        print("Chapters found in description:")
        for chapter in chapters:
            print(chapter)
    else:
        print("No chapters found in the description.")

    # Fetch and process the transcript
    processor.process_transcript(include_timestamps=True)
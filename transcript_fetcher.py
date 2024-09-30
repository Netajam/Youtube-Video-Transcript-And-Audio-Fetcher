from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from file_utils import MarkdownWriter
from config import templates_path
class TranscriptFetcher:
    def __init__(self, youtube_client):
        self.youtube = youtube_client
        self.markdown_writer=MarkdownWriter()
    def get_video_transcript(self,video_id,video_title, include_timestamps=False):
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript(['en']).fetch()
            if include_timestamps:
                transcript_text = '\n'.join([f"[{self.format_timestamp(item['start'])}] {item['text']}" for item in transcript])
            else:
                transcript_text = ' '.join([item['text'] for item in transcript])
            return transcript_text
        except (TranscriptsDisabled, NoTranscriptFound):
            return 'Transcript not available'

    def format_timestamp(self,seconds):
        return f"{int(seconds // 3600):02d}:{int((seconds % 3600) // 60):02d}:{int(seconds % 60):02d}"


    def save_full_transcript2md(self,video_id,video_title, include_timestamps=False):

        transcript = self.get_video_transcript(video_id, include_timestamps, video_title)
        if transcript != 'Transcript not available':
            
            self.markdown_writer.save_transcript_to_markdown(video_id, transcript, video_title, include_timestamps)
            self.markdown_writer.save_video_link_to_markdown(video_id, video_title)
        else:
            print(f"Unable to fetch transcript for video ID {video_id}.")

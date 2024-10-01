from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from file_utils import MarkdownWriter
class TranscriptFetcher:
    _NO_TRANSCRIPT='Transcript not available'
    
    def __init__(self, youtube_client):
        self.youtube = youtube_client
        self.markdown_writer=MarkdownWriter()

    def fetch_transcript(self,video_id, include_timestamps=False):
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript(['en']).fetch()
            if include_timestamps:
                transcript_text = '\n'.join([f"[{self.format_timestamp(item['start'])}] {item['text']}" for item in transcript])
            else:
                transcript_text = ' '.join([item['text'] for item in transcript])
            return transcript_text
        except (TranscriptsDisabled, NoTranscriptFound):
            return TranscriptFetcher._NO_TRANSCRIPT

    def format_timestamp(self,seconds):
        return f"{int(seconds // 3600):02d}:{int((seconds % 3600) // 60):02d}:{int(seconds % 60):02d}"


    def create_md_files(self,video_id,video_title, include_timestamps=False):

        transcript = self.fetch_transcript(video_id, include_timestamps)
        if transcript != TranscriptFetcher._NO_TRANSCRIPT:
            
            self.markdown_writer.format_save_transcript(video_id, transcript, video_title, include_timestamps)
            self.markdown_writer.format_save_summary(video_id, video_title)
        else:
            print(f"No transcript to save for video: {video_id}.")
            
    def create_transcript_file(self,video_id,video_title, include_timestamps=False):

        transcript = self.fetch_transcript(video_id, include_timestamps)
        if transcript != TranscriptFetcher._NO_TRANSCRIPT:
            
            self.markdown_writer.format_save_transcript(video_id, transcript, video_title, include_timestamps)
        else:
            print(f"No transcript to save for video: {video_id}.")

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from file_utils import save_transcript_to_markdown, save_video_link_to_markdown

class TranscriptFetcher:
    def __init__(self, youtube_client):
        self.youtube = youtube_client
    def get_video_transcript(self,video_id, include_timestamps=False):
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

    def get_video_title(self,video_id):
        video_response = self.youtube.videos().list(id=video_id, part='snippet').execute()
        title = video_response['items'][0]['snippet']['title']
        return title

    def process_video_transcript_to_markdown(self,video_id, include_timestamps=False):
        transcript = self.get_video_transcript(video_id, include_timestamps)
        if transcript != 'Transcript not available':
            title = self.get_video_title(video_id)
            save_transcript_to_markdown(video_id, transcript, title, include_timestamps)
            save_video_link_to_markdown(video_id, title)
        else:
            print(f"Unable to fetch transcript for video ID {video_id}.")

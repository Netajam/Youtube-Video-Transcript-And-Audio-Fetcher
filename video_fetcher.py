from transcript_fetcher import TranscriptFetcher
from video_details_fetcher import YouTubeVideoProcessor
from prompt_generator import PromptGenerator
from playlists import Playlist
from gpt_summarizer import GPTSummarizer  # Import GPTSummarizer
import asyncio
from file_utils import sanitize_filename

class VideoFetcher:
    def __init__(self, video_id, youtube_client,openai_api_key=None):
        self.video_id = video_id
        self.youtube = youtube_client
        self.openai_api_key=openai_api_key
        self.transcript_fetcher = TranscriptFetcher(self.youtube)
        self.youtube_video_processor = YouTubeVideoProcessor(self.video_id, self.youtube)
        self.prompt_generator = PromptGenerator(32000)
        self.playlist = Playlist(self.youtube)
        self.gpt_summarizer = GPTSummarizer(self.openai_api_key)  # Initialize GPTSummarizer
    def set_openai_api_key(self, new_api_key):
        self._openai_api_key = new_api_key
        # Update the API key in the GPTSummarizer instance as well
        self.gpt_summarizer.set_openai_api_key(new_api_key)
    def get_openai_api_key(self):
        return self._openai_api_key
    def get_video_title(self,video_id):
        video_response = self.youtube.videos().list(id=video_id, part='snippet').execute()
        title = video_response['items'][0]['snippet']['title']
        return title

    def fetch_single_transcript(self,video_id, include_timestamps=False, generate_prompt=False, generate_gpt_summary=False):
        """
        Fetch a single transcript and optionally generate prompts and GPT summaries.
        """
        video_title = self.get_video_title(video_id)
        video_title=sanitize_filename(video_title)
        # Fetch and save the transcript to markdown
        self.transcript_fetcher.save_full_transcript2md(self.video_id,video_title, include_timestamps)

        # If the generate_prompt flag is set, generate the prompt markdown files
        if generate_prompt or generate_gpt_summary:
            print("Generating markdown files with prompts...")

            # Get the transcript and chapters
            transcript_with_timestamps = self.transcript_fetcher.get_video_transcript(self.video_id,video_title, include_timestamps=True)
            chapters = self.youtube_video_processor.extract_chapters_from_description()

            # Create PromptGenerator instance and split the transcript
            parsed_transcript = self.prompt_generator.parse_transcript_with_timestamps(transcript_with_timestamps)
            transcript_parts_with_chapters = self.prompt_generator.split_by_chapters_or_limit(parsed_transcript, chapters)

            # Generate the markdown prompt files
            self.prompt_generator.generate_markdown_files(transcript_parts_with_chapters,video_title)

            print("Prompt generation completed.")

        # If the generate_gpt_summary flag is set, call GPT summarizer
        if generate_gpt_summary:
            print("Running GPT summarizer on generated prompts...")
            asyncio.run(self.gpt_summarizer.process_prompt_files(video_title))  # Call GPTSummarizer to process prompts
            print("GPT summarization completed.")

    def fetch_multiple_transcripts(self, video_ids,include_timestamps=False):
        for video_id in video_ids:
            video_title=self.get_video_title(video_id)
            self.transcript_fetcher.save_full_transcript2md(video_id,video_title,include_timestamps)

    def fetch_channel_transcripts(self, channel_id, include_timestamps=False):
        uploads_playlist_id = self.playlist.get_uploads_playlist_id(channel_id)
        videos = self.playlist.get_playlist_videos(uploads_playlist_id)
        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            video_title=self.get_video_title(video_id)
            self.transcript_fetcher.save_full_transcript2md(video_id,video_title, include_timestamps)

    def fetch_playlist_transcripts(self, playlist_id, include_timestamps=False):
        videos = self.playlist.get_playlist_videos(playlist_id)
        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            video_title=self.get_video_title(video_id)
            self.transcript_fetcher.save_full_transcript2md(video_id,video_title, include_timestamps)

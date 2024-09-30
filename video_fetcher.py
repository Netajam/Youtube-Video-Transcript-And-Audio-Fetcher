from transcript_fetcher import TranscriptFetcher
from video_details_fetcher import YouTubeVideoProcessor
from prompt_generator import PromptGenerator
from playlists import Playlist

class VideoFetcher:
    def __init__(self, video_id, youtube_client):
        self.video_id = video_id
        self.youtube = youtube_client
        self.transcript_fetcher=TranscriptFetcher(self.youtube)
        self.youtube_video_processor= YouTubeVideoProcessor(self.video_id,self.youtube)
        self.prompt_generator= PromptGenerator(32000)
        self.playlist=Playlist(self.youtube)
    def fetch_single_transcript(self, include_timestamps=False, generate_prompt=False):
        """
        Fetch a single transcript and optionally generate prompts if the `generate_prompt` flag is set.
        """
        # Fetch and save the transcript to markdown
        self.transcript_fetcher.process_video_transcript_to_markdown(self.video_id,include_timestamps)

        # If the generate_prompt flag is set, generate the prompt markdown files
        if generate_prompt:
            print("Generating markdown files with prompts...")

            # Get the transcript and chapters
            transcript_with_timestamps = self.transcript_fetcher.get_video_transcript(self.video_id,include_timestamps=True)
            chapters = self.youtube_video_processor.extract_chapters_from_description()

            # Create PromptGenerator instance and split the transcript
            parsed_transcript = self.prompt_generator.parse_transcript_with_timestamps(transcript_with_timestamps)
            transcript_parts_with_chapters = self.prompt_generator.split_by_chapters_or_limit(parsed_transcript, chapters)

            # Generate the markdown prompt files
            self.prompt_generator.generate_markdown_files(transcript_parts_with_chapters)

            print("Prompt generation completed.")

    def fetch_multiple_transcripts(self,video_ids, include_timestamps=False):
        for video_id in video_ids:
            self.transcript_fetcher.process_video_transcript_to_markdown(video_id, include_timestamps)

    def fetch_channel_transcripts(self,channel_id, include_timestamps=False):
        uploads_playlist_id = self.playlist.get_uploads_playlist_id(channel_id)
        videos = self.playlist.get_playlist_videos(uploads_playlist_id)
        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            self.transcript_fetcher.process_video_transcript_to_markdown(video_id, include_timestamps)

    def fetch_playlist_transcripts(self,playlist_id, include_timestamps=False):
        videos = self.playlist.get_playlist_videos(playlist_id)
        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            self.transcript_fetcher.process_video_transcript_to_markdown(video_id, include_timestamps)

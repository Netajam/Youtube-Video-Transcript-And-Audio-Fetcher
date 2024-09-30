import argparse
from config import video_id, video_ids, channel_id, playlist_id
from video_fetcher import VideoFetcher
from audio_downloader import AudioDownloader
import os
from dotenv import load_dotenv 
from googleapiclient.discovery import build
def main():
    load_dotenv()
    api_key = os.environ.get("youtube_api_key")
    youtube = build('youtube', 'v3', developerKey=api_key)
    parser = argparse.ArgumentParser(description='YouTube Transcript Downloader and Audio Downloader')
    parser.add_argument('-mul', '--multiple', action='store_true', help='Download multiple transcripts')
    parser.add_argument('-ch', '--channel', action='store_true', help='Download all transcripts from a YouTube channel')
    parser.add_argument('-pl', '--playlist', action='store_true', help='Download all transcripts from a YouTube playlist')
    parser.add_argument('-ts', '--timestamps', action='store_true', help='Include timestamps in the downloaded transcripts')
    parser.add_argument('-ad', '--audio', action='store_true', help='Download the associated MP3 files')
    parser.add_argument('-gp', '--generate_prompt', action='store_true', help='Generate markdown files for the transcript with prompt instructions')  # New flag for prompt generation
    args = parser.parse_args()

    if args.audio:
        audio_downloader=AudioDownloader(youtube)
        if args.multiple:
            audio_downloader.download_multiple_audios(video_ids)
        elif args.channel:
            audio_downloader.download_channel_audios(channel_id)
        elif args.playlist:
            audio_downloader.download_playlist_audios(playlist_id)
        else:
            audio_downloader.download_single_audio(video_id)
    else:
        video_fetcher=VideoFetcher(video_id, youtube)
        if args.multiple:
            video_fetcher.fetch_multiple_transcripts(video_ids, args.timestamps)
        elif args.channel:
            video_fetcher.fetch_channel_transcripts(channel_id, args.timestamps)
        elif args.playlist:
            video_fetcher.fetch_playlist_transcripts(playlist_id, args.timestamps)
        else:
            video_fetcher.fetch_single_transcript(args.timestamps, args.generate_prompt)  # Pass generate_prompt flag

if __name__ == "__main__":

    main()
import argparse
from config import VIDEO_ID, VIDEO_IDS, CHANNEL_ID, PLAYLIST_ID
from youtube_media_fetcher import YoutubeMediaFetcher
from audio_downloader import AudioDownloader
from gpt_summarizer import GPTSummarizer  # Import the GPTSummarizer class
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
    parser.add_argument('-gp', '--generate_prompt', action='store_true', help='Generate markdown files for the transcript with prompt instructions')
    parser.add_argument('-gpt', '--generate_gpt_summary', action='store_true', help='Generate markdown files with prompts and run GPT summarization')  # New flag for GPT summarization

    args = parser.parse_args()

    if args.audio:
        audio_downloader = AudioDownloader(youtube)
        if args.multiple:
            audio_downloader.download_multiple_audios(VIDEO_IDS)
        elif args.channel:
            audio_downloader.download_channel_audios(CHANNEL_ID)
        elif args.playlist:
            audio_downloader.download_playlist_audios(PLAYLIST_ID)
        else:
            audio_downloader.download_single_audio(VIDEO_ID)
    else:
        video_fetcher = YoutubeMediaFetcher(VIDEO_ID, youtube)
        if args.multiple:
            video_fetcher.process_multiple_video(VIDEO_IDS, args.timestamps)
        elif args.channel:
            video_fetcher.process_channel(CHANNEL_ID, args.timestamps)
        elif args.playlist:
            video_fetcher.process_playlist(PLAYLIST_ID, args.timestamps)
        else:
            load_dotenv(override=True)
            openai_api_key = os.getenv("OPENAI_API_KEY")
            video_fetcher.set_openai_api_key(openai_api_key)
            print(video_fetcher.get_openai_api_key())
            video_fetcher.process_single_video(VIDEO_ID, args.timestamps, args.generate_prompt, args.generate_gpt_summary)  # Pass the new generate_gpt_summary flag

if __name__ == "__main__":
    main()

import argparse
from config import video_id, video_ids, channel_id, playlist_id
from transcript_fetcher import fetch_single_transcript, fetch_multiple_transcripts, fetch_channel_transcripts, fetch_playlist_transcripts
from audio_downloader import download_single_audio, download_multiple_audios, download_channel_audios, download_playlist_audios

def main():
    parser = argparse.ArgumentParser(description='YouTube Transcript Downloader and Audio Downloader')
    parser.add_argument('-mul', '--multiple', action='store_true', help='Download multiple transcripts')
    parser.add_argument('-ch', '--channel', action='store_true', help='Download all transcripts from a YouTube channel')
    parser.add_argument('-pl', '--playlist', action='store_true', help='Download all transcripts from a YouTube playlist')
    parser.add_argument('-ts', '--timestamps', action='store_true', help='Include timestamps in the downloaded transcripts')
    parser.add_argument('-ad', '--audio', action='store_true', help='Download the associated MP3 files')
    args = parser.parse_args()

    if args.audio:
        if args.multiple:
            download_multiple_audios(video_ids)
        elif args.channel:
            download_channel_audios(channel_id)
        elif args.playlist:
            download_playlist_audios(playlist_id)
        else:
            download_single_audio(video_id)
    else:
        if args.multiple:
            fetch_multiple_transcripts(video_ids, args.timestamps)
        elif args.channel:
            fetch_channel_transcripts(channel_id, args.timestamps)
        elif args.playlist:
            fetch_playlist_transcripts(playlist_id, args.timestamps)
        else:
            fetch_single_transcript(video_id, args.timestamps)

if __name__ == "__main__":
    main()
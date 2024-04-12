import argparse
from config import video_id, video_ids, channel_id, playlist_id
from transcript_fetcher import fetch_single_transcript, fetch_multiple_transcripts, fetch_channel_transcripts, fetch_playlist_transcripts

# main.py



def main():
    parser = argparse.ArgumentParser(description='YouTube Transcript Downloader')
    parser.add_argument('-mul', '--multiple', action='store_true', help='Download multiple transcripts')
    parser.add_argument('-ch', '--channel', action='store_true', help='Download all transcripts from a YouTube channel')
    parser.add_argument('-pl', '--playlist', action='store_true', help='Download all transcripts from a YouTube playlist')
    parser.add_argument('-ts', '--timestamps', action='store_true', help='Include timestamps in the downloaded transcripts')
    args = parser.parse_args()

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
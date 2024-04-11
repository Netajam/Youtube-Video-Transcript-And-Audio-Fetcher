import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from file_utils import save_transcript_to_markdown, sanitize_filename
from youtube_api import get_uploads_playlist_id, get_playlist_videos

api_key = os.environ.get("youtube_api_key")
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en']).fetch()
        return ' '.join([item['text'] for item in transcript])
    except (TranscriptsDisabled, NoTranscriptFound):
        return 'Transcript not available'

def get_video_title(video_id):
    video_response = youtube.videos().list(id=video_id, part='snippet').execute()
    title = video_response['items'][0]['snippet']['title']
    return title

def process_video_transcript_to_markdown(video_id):
    transcript = get_video_transcript(video_id)
    if transcript != 'Transcript not available':
        title = get_video_title(video_id)
        save_transcript_to_markdown(video_id, transcript, title)
    else:
        print(f"Unable to fetch transcript for video ID {video_id}.")

def fetch_single_transcript(video_id):
    process_video_transcript_to_markdown(video_id)

def fetch_multiple_transcripts(video_ids):
    for video_id in video_ids:
        process_video_transcript_to_markdown(video_id)

def fetch_channel_transcripts(channel_id):
    uploads_playlist_id = get_uploads_playlist_id(channel_id, youtube)
    videos = get_playlist_videos(uploads_playlist_id, youtube)
    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        process_video_transcript_to_markdown(video_id)

def fetch_playlist_transcripts(playlist_id):
    videos = get_playlist_videos(playlist_id, youtube)
    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        process_video_transcript_to_markdown(video_id)

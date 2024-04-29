import os
from pytube import YouTube
from youtube_api import get_uploads_playlist_id, get_playlist_videos
from googleapiclient.discovery import build


api_key = os.environ.get("youtube_api_key")
youtube = build('youtube', 'v3', developerKey=api_key)
def create_audio_folder():
    audio_folder = "generated_audio"
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    return audio_folder

def download_audio(video_url, output_path):
    try:
        video = YouTube(video_url)
        audio_stream = video.streams.filter(only_audio=True).first()
        print(f"Downloading audio from {video.title}...")
        audio_stream.download(output_path)
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def download_single_audio(video_id):
    audio_folder = create_audio_folder()
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    download_audio(video_url, audio_folder)

def download_multiple_audios(video_ids):
    audio_folder = create_audio_folder()
    for video_id in video_ids:
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        download_audio(video_url, audio_folder)

def download_channel_audios(channel_id):
    audio_folder = create_audio_folder()
    uploads_playlist_id = get_uploads_playlist_id(channel_id, youtube)
    videos = get_playlist_videos(uploads_playlist_id, youtube)
    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        download_audio(video_url, audio_folder)

def download_playlist_audios(playlist_id):
    audio_folder = create_audio_folder()
    videos = get_playlist_videos(playlist_id, youtube)
    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        download_audio(video_url, audio_folder)
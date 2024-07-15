import os
from pytube import YouTube
from youtube_api import get_uploads_playlist_id, get_playlist_videos
from googleapiclient.discovery import build
from moviepy.editor import AudioFileClip
from config import audio_files_path

api_key = os.environ.get("youtube_api_key")
youtube = build('youtube', 'v3', developerKey=api_key)

def create_audio_folder():
    if not os.path.exists(audio_files_path):
        os.makedirs(audio_files_path)
    return audio_files_path

def download_audio(video_url, output_path):
    try:
        video = YouTube(video_url)
        audio_stream = video.streams.filter(only_audio=True).order_by('abr').last()
        print(f"Downloading audio from {video.title}...")
        
        # Download the audio stream as WebM
        audio_file_path = audio_stream.download(output_path)
        
        # Convert WebM to MP3 using moviepy
        audio_clip = AudioFileClip(audio_file_path)
        mp3_file_path = os.path.splitext(audio_file_path)[0] + ".mp3"
        audio_clip.write_audiofile(mp3_file_path)
        audio_clip.close()
        
        # Remove the original WebM file
        os.remove(audio_file_path)
        
        print("Audio downloaded and converted to MP3 successfully!")
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
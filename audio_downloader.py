import os
from pytube import YouTube
from playlists import Playlist
from moviepy import AudioFileClip
from config import AUDIO_FILES_DIR


class AudioDownloader:
    def __init__(self, youtube_client):
        self.youtube=youtube_client
        self.playlist=Playlist(self.youtube)

    def create_audio_folder():
        if not os.path.exists(AUDIO_FILES_DIR):
            os.makedirs(AUDIO_FILES_DIR)
        return AUDIO_FILES_DIR

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

    def download_single_audio(self,video_id):
        audio_folder = self.create_audio_folder()
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        self.download_audio(video_url, audio_folder)

    def download_multiple_audios(self,video_ids):
        audio_folder = self.create_audio_folder()
        for video_id in video_ids:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            self.download_audio(video_url, audio_folder)

    def download_channel_audios(self,channel_id):
        audio_folder = self.create_audio_folder()
        uploads_playlist_id = self.get_uploads_playlist_id(channel_id, self.youtube)
        videos = self.get_playlist_videos(uploads_playlist_id, self.youtube)
        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            self.download_audio(video_url, audio_folder)

    def download_playlist_audios(self,playlist_id):
        audio_folder = self.create_audio_folder()
        videos = self.playlist.get_playlist_videos(playlist_id, self.youtube)
        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            self.download_audio(video_url, audio_folder)
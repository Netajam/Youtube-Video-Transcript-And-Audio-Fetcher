from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("youtube_api_key")

def get_uploads_playlist_id(channel_id, youtube):
    response = youtube.channels().list(id=channel_id, part='contentDetails').execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_playlist_videos(playlist_id, youtube):
    videos = []
    next_page_token = None

    while True:
        response = youtube.playlistItems().list(
            playlistId=playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token).execute()

        videos += response['items']
        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return videos

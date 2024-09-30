from googleapiclient.discovery import build
import os

class Playlist:
    def __init__(self,youtube_client):
        self.youtube=youtube_client
    def get_uploads_playlist_id(self,channel_id):
        response = self.youtube.channels().list(id=channel_id, part='contentDetails').execute()
        return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    def get_playlist_videos(self,playlist_id):
        videos = []
        next_page_token = None

        while True:
            response = self.youtube.playlistItems().list(
                playlistId=playlist_id,
                part='snippet',
                maxResults=50,
                pageToken=next_page_token).execute()

            videos += response['items']
            next_page_token = response.get('nextPageToken')

            if not next_page_token:
                break

        return videos

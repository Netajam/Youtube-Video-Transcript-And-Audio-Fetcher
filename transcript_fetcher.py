import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from file_utils import save_transcript_to_markdown, sanitize_filename, save_video_link_to_markdown, save_merged_transcript_to_markdown
from youtube_api import get_uploads_playlist_id, get_playlist_videos
from config import language_to_fetch, is_second_language, second_language_to_fetch, merged_transcript_files_path
import re
from datetime import timedelta
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from xml.etree.ElementTree import ParseError
api_key = os.environ.get("youtube_api_key")
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_transcript(video_id, language, include_timestamps=False):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript([language]).fetch()
        
        if include_timestamps:
            transcript_text = '\n'.join([f"[{format_timestamp(item['start'])}] {item['text']}" for item in transcript])
        else:
            transcript_text = ' '.join([item['text'] for item in transcript])
        
        return transcript_text
    
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        print(f"Transcript not available for video ID {video_id}: {str(e)}")
        return 'Transcript not available'
    
    except ParseError as e:
        print(f"Error parsing transcript for video ID {video_id}: {str(e)}")
        return 'Error parsing transcript'
    
    except Exception as e:
        print(f"Unexpected error occurred for video ID {video_id}: {str(e)}")
        return 'Unexpected error occurred'
def format_timestamp(seconds):
    return f"{int(seconds // 3600):02d}:{int((seconds % 3600) // 60):02d}:{int(seconds % 60):02d}"

def get_video_title(video_id):
    video_response = youtube.videos().list(id=video_id, part='snippet').execute()
    title = video_response['items'][0]['snippet']['title']
    return title

def process_video_transcript_to_markdown(video_id, include_timestamps=False):
    transcript1 = get_video_transcript(video_id, language_to_fetch, include_timestamps=True)
    
    if transcript1 in ['Transcript not available', 'Error parsing transcript', 'Unexpected error occurred']:
        print(f"Skipping video ID {video_id} due to error: {transcript1}")
        return
    
    title = get_video_title(video_id)
    save_transcript_to_markdown(video_id, transcript1, title, language_to_fetch, include_timestamps)
    save_video_link_to_markdown(video_id, title)
    
    if is_second_language:
        transcript2 = get_video_transcript(video_id, second_language_to_fetch, include_timestamps=True)
        
        if transcript2 not in ['Transcript not available', 'Error parsing transcript', 'Unexpected error occurred']:
            save_transcript_to_markdown(video_id, transcript2, title, second_language_to_fetch, include_timestamps)
            
            merged_transcript = merge_transcripts(transcript1, transcript2, include_timestamps)
            save_merged_transcript_to_markdown(video_id, merged_transcript, title, language_to_fetch, second_language_to_fetch, include_timestamps)
        else:
            print(f"Unable to fetch second language transcript for video ID {video_id}. Reason: {transcript2}")
def parse_timestamp(timestamp_str):
    # Convert timestamp string to seconds
    h, m, s = map(float, timestamp_str.strip('[]').split(':'))
    return timedelta(hours=h, minutes=m, seconds=s).total_seconds()

def format_timestamp(seconds):
    # Convert seconds back to timestamp string
    return f"{int(seconds // 3600):02d}:{int((seconds % 3600) // 60):02d}:{int(seconds % 60):02d}"

def parse_transcript(transcript):
    # Parse the transcript into a dictionary with timestamps as keys
    parsed = {}
    current_timestamp = 0
    current_text = []

    for line in transcript.split('\n'):
        timestamp_match = re.match(r'\[(\d{2}:\d{2}:\d{2})\]', line)
        if timestamp_match:
            if current_text:
                parsed[current_timestamp] = ' '.join(current_text)
                current_text = []
            current_timestamp = parse_timestamp(timestamp_match.group(1))
            text = line[timestamp_match.end():].strip()
            if text:
                current_text.append(text)
        else:
            current_text.append(line.strip())

    if current_text:
        parsed[current_timestamp] = ' '.join(current_text)

    return parsed

def merge_transcripts(transcript1, transcript2, include_timestamps=True):
    parsed1 = parse_transcript(transcript1)
    parsed2 = parse_transcript(transcript2)

    # Combine all timestamps from both transcripts
    all_timestamps = sorted(set(parsed1.keys()) | set(parsed2.keys()))

    merged_lines = []
    for timestamp in all_timestamps:
        formatted_timestamp = f"[{format_timestamp(timestamp)}]"
        text1 = parsed1.get(timestamp, '')
        text2 = parsed2.get(timestamp, '')

        if include_timestamps:
            merged_lines.append(f"{formatted_timestamp} {text1}")
            merged_lines.append(f"{formatted_timestamp} {text2}")
        else:
            merged_lines.append(text1)
            merged_lines.append(text2)

        # Add a blank line between timestamp groups for better readability
        merged_lines.append('')

    return '\n'.join(merged_lines).strip()
def fetch_single_transcript(video_id, include_timestamps=False):
    process_video_transcript_to_markdown(video_id, include_timestamps)

def fetch_multiple_transcripts(video_ids, include_timestamps=False):
    for video_id in video_ids:
        process_video_transcript_to_markdown(video_id, include_timestamps)

def fetch_channel_transcripts(channel_id, include_timestamps=False):
    uploads_playlist_id = get_uploads_playlist_id(channel_id, youtube)
    videos = get_playlist_videos(uploads_playlist_id, youtube)
    
    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        try:
            process_video_transcript_to_markdown(video_id, include_timestamps)
        except Exception as e:
            print(f"Error processing video ID {video_id}: {str(e)}. Continuing with next video.")
def fetch_playlist_transcripts(playlist_id, include_timestamps=False):
    videos = get_playlist_videos(playlist_id, youtube)
    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        process_video_transcript_to_markdown(video_id, include_timestamps)
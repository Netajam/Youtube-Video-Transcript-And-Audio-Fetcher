# YouTube Transcript Downloader and Audio Downloader

This tool allows you to download transcripts and audio files from YouTube videos. You can download transcripts and audio for a single video, multiple videos, all videos from a YouTube channel, or all videos from a YouTube playlist.

## Features

- Download transcripts as Markdown files
- Download audio files as MP3
- Support for single video, multiple videos, YouTube channel, and YouTube playlist
- Option to include timestamps in the downloaded transcripts

## Prerequisites

Before using this tool, make sure you have the following:
- Python 3.x installed
- Google YouTube API key

## Setup

1. Clone the repository:
git clone https://github.com/RenardDuDesert/Youtube-Video-Transcript-Fetcher.git
Copy code
2. Navigate to the project directory.
3. (Optional but recommended) Create a Python virtual environment using `python3 -m venv venv`. This step is optional but highly recommended to keep the project's dependencies isolated from the system-wide Python installation.
4. Activate the virtual environment using the appropriate command for the operating system:
- On Windows: `venv\Scripts\activate`
- On macOS and Linux: `source venv/bin/activate`
5. Install the required dependencies using `pip install -r requirements.txt`. This command reads the `requirements.txt` file and installs all the listed packages.
6. Set the Google YouTube API key as an environment variable.

## Configuration

Create a `config.py` file in the project directory and add the following variables:
```python
# config.py

# Single video ID
video_id = 'video_id'

# Multiple video IDs
video_ids = ['video_id_1', 'video_id_2', ...]

# Channel ID
channel_id = 'channel_id'

# Playlist ID
playlist_id = 'playlist_id'
```

Replace 'video_id', 'video_id_1', 'video_id_2', 'channel_id', and 'playlist_id' with the actual video IDs, channel ID, and playlist ID you want to download transcripts and audio for.
Usage

Download transcript and audio for a single video:

Set the video_id variable in config.py to the desired video ID.
Run the following command to download the transcript:
 python main.py

Run the following command to download the audio:
 python main.py -ad



Download transcripts and audio for multiple videos:

Fill the video_ids list in config.py with the desired video IDs.
Run the following command to download the transcripts:
 python main.py -mul

Run the following command to download the audio files:
 python main.py -ad -mul



Download all transcripts and audio from a YouTube channel:

Set the channel_id variable in config.py to the desired channel ID.
Run the following command to download the transcripts:
 python main.py -ch

Run the following command to download the audio files:
 python main.py -ad -ch



Download all transcripts and audio from a YouTube playlist:

Set the playlist_id variable in config.py to the desired playlist ID.
Run the following command to download the transcripts:
 main.py -pl

Run the following command to download the audio files:
 main.py -ad -pl



To include timestamps in the downloaded transcripts, add the -ts or --timestamps flag when running the script.

The transcripts will be saved as Markdown files in the project directory with sanitized filenames. The audio files will be saved as MP3 files in the generated_audio folder within the project directory.
Notes

Make sure you have a valid Google YouTube API key and have enabled the YouTube Data API in your Google Developer Console.
The tool uses the youtube_transcript_api library to fetch transcripts. If a transcript is not available for a video, it will skip that video and move on to the next one.
The filenames of the Markdown files are sanitized to remove any characters that are not allowed in filenames.
The audio files are downloaded using the pytube library. Make sure you have it installed (pip install pytube).

If you have any questions or issues, please feel free to open an issue in the repository.
Finding Video ID, Channel ID, and Playlist ID
To use this tool, you need to provide the video ID of a YouTube video, the channel ID of a YouTube channel, or the playlist ID of a YouTube playlist. Here's how you can find them:
Finding the Video ID

Open the YouTube video in your web browser.
Look at the URL of the video. The video ID is the string of characters after v= in the URL.
For example, in the URL https://www.youtube.com/watch?v=abc123, the video ID is abc123.

Finding the Channel ID

Open the YouTube channel in your web browser.
Click on the channel's profile picture to go to the channel's page.
Look at the URL of the channel page. The channel ID is the string of characters after channel/ in the URL.
For example, in the URL https://www.youtube.com/channel/UCabcdef123, the channel ID is UCabcdef123.

Alternatively, you can find the channel ID using the YouTube API:

Open the YouTube channel in your web browser.
View the page source (right-click on the page and select "View Page Source" or use the keyboard shortcut Ctrl+U on Windows or Command+U on Mac).
Search for channelId in the page source. You should find a line that looks like this:
htmlCopy code"channelId":"UCabcdef123"


Finding the Playlist ID

Open the YouTube playlist in your web browser.
Look at the URL of the playlist. The playlist ID is the string of characters after list= in the URL.
For example, in the URL https://www.youtube.com/playlist?list=PLabcdef123, the playlist ID is PLabcdef123.

Once you have the video ID, channel ID, or playlist ID, you can add them to the config.py file as mentioned in the Configuration section.
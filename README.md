# YouTube Transcript Downloader and Audio Downloader

This tool allows you to download transcripts and audio files from YouTube videos. You can download transcripts and audio for a single video, multiple videos, all videos from a YouTube channel, or all videos from a YouTube playlist.

## Features

- Download transcripts as Markdown files
- Generate summary files for transcripts
- Download audio files as MP3
- Support for single video, multiple videos, YouTube channel, and YouTube playlist
- Option to include timestamps in the downloaded transcripts
- Use of customizable templates for transcript and summary files

## Prerequisites

Before using this tool, make sure you have the following:
- Python 3.x installed
- Google YouTube API key

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Netajam/Youtube-Video-Transcript-Fetcher.git
   ```
2. Navigate to the project directory.
3. (Optional but recommended) Create a Python virtual environment using `python3 -m venv venv`.
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the required dependencies using `pip install -r requirements.txt`.
6. Set the Google YouTube API key as an environment variable.
   - Create a `.env` file with the 'youtube_api_key = "YOUR_YOUTUBE_API_KEY"
## Configuration

Use the config.py file to put the values of the video_id, channel_id, playlist_id that you want to fetch.Create a `config.py` file in the project directory and add the following variables:
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

## Templates

The templates for the transcript and summary markdown files are located in the `templates` folder:

- `transcript_template.md`: Template for the transcript file
- `summary_template.md`: Template for the summary file

You can customize these templates to change the structure of the generated markdown files.

## Usage

When you run the script, it generates two files for each video:
1. A transcript file containing the full transcript of the video
2. A summary file where you can add a summary of the transcript

Download transcript and audio for a single video:

1. Set the `video_id` variable in `config.py` to the desired video ID.
2. Run the following command to download the transcript and generate the summary file:
   ```
   python main.py
   ```
3. Run the following command to download the audio:
   ```
   python main.py -ad
   ```

[The rest of the usage instructions remain the same as in the original README]

## Notes

- Make sure you have a valid Google YouTube API key and have enabled the YouTube Data API in your Google Developer Console.
- The tool uses the youtube_transcript_api library to fetch transcripts. If a transcript is not available for a video, it will skip that video and move on to the next one.
- The filenames of the Markdown files are sanitized to remove any characters that are not allowed in filenames.
- The audio files are downloaded using the pytube library. Make sure you have it installed (`pip install pytube`).
- The transcript and summary files are generated based on the templates in the `templates` folder. You can customize these templates to suit your needs.

If you have any questions or issues, please feel free to open an issue in the repository.


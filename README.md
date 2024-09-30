Here’s an updated version of the README file that incorporates the new functionalities you’ve added, including clearing the output directory before generating the new transcript markdown files, and handling GPT summaries.

### Updated README

# YouTube Transcript Downloader and Audio Downloader

This tool allows you to download transcripts and audio files from YouTube videos, generate summaries using OpenAI's GPT models, and handle files in a more structured way. You can download transcripts and audio for a single video, multiple videos, all videos from a YouTube channel, or all videos from a YouTube playlist.

## Features

- Download transcripts as Markdown files
- Generate summary files for transcripts using GPT
- Download audio files as MP3
- Support for single video, multiple videos, YouTube channel, and YouTube playlist
- Option to include timestamps in the downloaded transcripts
- Automatic clearing of the transcript directory to ensure only the relevant files are processed for GPT summary generation
- Use of customizable templates for transcript and summary files

## Prerequisites

Before using this tool, make sure you have the following:
- Python 3.x installed
- Google YouTube API key
- OpenAI API key for GPT summaries

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Netajam/Youtube-Video-Transcript-Fetcher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Youtube-Video-Transcript-Fetcher
   ```
3. (Optional but recommended) Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set up the environment variables:
   - Create a `.env` file in the root of the project directory and add your YouTube API and OpenAI API keys:
     ```bash
     youtube_api_key = "YOUR_YOUTUBE_API_KEY"
     openai_api_key = "YOUR_OPENAI_API_KEY"
     ```

## Configuration

Configure the tool by setting the video, channel, or playlist details in `config.py`:

```python
# config.py

# Single video ID
video_id = 'O9upVbGSBFo'

# Multiple video IDs
video_ids = ['abc123', 'def456', 'ghi789']

# Channel ID
channel_id = 'UCQNsB8n2QhRzjdfjyZ_2S_g'

# Playlist IDs
playlist_id = 'PLAzuPFpwy9ZLIG5hDwjGyccJr6FpTsrEr'

# File paths
transcript_files_path = 'transcripts'  # Path where transcript files will be saved
summary_files_path = 'summaries'  # Path where summary files will be saved
audio_files_path = 'audio'  # Path where audio files will be saved
templates_path = 'templates'  # Path where template files are located
transcript_parts_dir = 'temp/transcript_parts'  # Path for temporary transcript parts
gpt_summaries = 'summaries_gpt'  # Path for GPT summary files

# Template file names
transcript_template_file = 'transcript_template.md'
summary_template_file = 'summary_template.md'

# Transcript settings
language_to_fetch = 'en'

# GPT model configuration
openai_model = "gpt-4o"
```

## Templates

The templates for the transcript and summary markdown files are located in the `templates` folder:

- `transcript_template.md`: Template for the transcript file.
- `summary_template.md`: Template for the summary file.

You can customize these templates to change the structure of the generated markdown files.

## New Functionalities

1. **Clearing Output Directory**: Before generating transcript markdown files, the tool ensures that the output directory (e.g., `temp/transcript_prompts`) is cleared of all files and subdirectories. This ensures that only the current transcript parts are processed.
   
   This prevents mixing old and new files, which is important when generating GPT summaries, ensuring that the files processed are only related to the current task.

2. **Generate GPT Summaries**: After generating transcript markdown files, the tool can send requests to OpenAI's API to generate summaries for the transcript parts. It monitors the OpenAI API's token limits to ensure compliance.

## Usage

### Download transcript and audio for a single video

1. Set the `video_id` variable in `config.py` to the desired video ID.
2. Run the following command to download the transcript and generate the summary file:
   ```bash
   python main.py
   ```
3. Run the following command to download the audio:
   ```bash
   python main.py -ad
   ```

### Download transcripts and audio for multiple videos

1. Set the `video_ids` variable in `config.py` to a list of video IDs.
2. Run the following command:
   ```bash
   python main.py -mv
   ```

### Download transcripts and audio for all videos in a channel

1. Set the `channel_id` variable in `config.py` to the desired YouTube channel ID.
2. Run the following command:
   ```bash
   python main.py -c
   ```

### Download transcripts and audio for all videos in a playlist

1. Set the `playlist_id` variable in `config.py` to the desired YouTube playlist ID.
2. Run the following command:
   ```bash
   python main.py -pl
   ```

### Generating GPT Summaries

To generate summaries using GPT after the transcripts have been downloaded and processed:
1. Ensure the OpenAI API key is set in the `.env` file.
2. Set the `openai_model` and other GPT-related configurations in `config.py`.
3. Run the script to generate summaries:
   ```bash
   python main.py --gpt
   ```

The script will clear the output directory, generate new transcript parts, and send them to OpenAI for summarization.

## Notes

- Make sure you have a valid Google YouTube API key and OpenAI API key.
- The tool uses the `youtube_transcript_api` library to fetch transcripts. If a transcript is not available for a video, it will skip that video and move on to the next one.
- The audio files are downloaded using the `pytube` library. Ensure it's installed by running `pip install pytube`.
- The filenames of the Markdown files are sanitized to remove any characters that are not allowed in filenames.
- The transcript and summary files are generated based on the templates in the `templates` folder. You can customize these templates to suit your needs.

If you have any questions or issues, feel free to open an issue in the repository.
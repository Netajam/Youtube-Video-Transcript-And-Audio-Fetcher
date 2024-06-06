import os
import re

def sanitize_filename(title):
    sanitized_title = re.sub(r'[<>:"/\\|?*]', '', title)
    sanitized_title = re.sub(r'\s+', ' ', sanitized_title)
    sanitized_title = sanitized_title.strip()
    return sanitized_title

def save_transcript_to_markdown(video_id, transcript, title, include_timestamps=False):
    sanitized_title = sanitize_filename(title)
    filename = f"Tr-{sanitized_title}.md"
    
    os.makedirs('generated_files', exist_ok=True)
    
    file_path = os.path.join('generated_files', filename)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(f"#  {title}\n\n")
        if include_timestamps:
            md_file.write(transcript)
        else:
            md_file.write(transcript.replace('\n', ' '))
    print(f"Transcript saved to {file_path}.")

def save_video_link_to_markdown(video_id, title):
    sanitized_title = sanitize_filename(title)
    filename = f"VD-SM-{sanitized_title}.md"
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    os.makedirs('summary', exist_ok=True)
    
    file_path = os.path.join('summary', filename)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# Video Link\n\n")
        md_file.write(f"[{title}]({video_url})\n")
    print(f"Video link saved to {file_path}.")

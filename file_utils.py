import os
import re

def sanitize_filename(title):
    sanitized_title = re.sub(r'[<>:"/\\|?*]', '', title)
    sanitized_title = re.sub(r'\s+', ' ', sanitized_title)
    sanitized_title = sanitized_title.strip()
    return sanitized_title

def save_transcript_to_markdown(video_id, transcript, title, include_timestamps=False):
    sanitized_title = sanitize_filename(title)
    filename = f"{sanitized_title}.md"
    
    os.makedirs('generated_files', exist_ok=True)
    
    file_path = os.path.join('generated_files', filename)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# {title}\n\n")
        if include_timestamps:
            md_file.write(transcript)
        else:
            md_file.write(transcript.replace('\n', ' '))
    print(f"Transcript saved to {file_path}.")

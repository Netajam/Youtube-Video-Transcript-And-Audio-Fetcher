import os
import re
from config import transcript_files_path, summary_files_path, templates_path, transcript_template_file, summary_template_file

def save_transcript_to_markdown(video_id, transcript, sanitized_title, include_timestamps=False):
    filename = f"Tr-{sanitized_title}.md"
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    os.makedirs(transcript_files_path, exist_ok=True)
    
    template_path = os.path.join(templates_path, transcript_template_file)
    template_content = read_template(template_path)
    
    if not include_timestamps:
        transcript = transcript.replace('\n', ' ')
    
    filled_template = template_content.format(
        title=sanitized_title,
        video_url=video_url,
        transcript=transcript
    )
    
    file_path = os.path.join(transcript_files_path, filename)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(filled_template)
    
    print(f"Transcript saved to {file_path}.")

def sanitize_filename(title):
    sanitized_title = re.sub(r'[<>:"/\\|?*]', '', title)
    sanitized_title = re.sub(r'\s+', ' ', sanitized_title)
    sanitized_title = sanitized_title.strip()
    return sanitized_title

def read_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as template_file:
        return template_file.read()

def save_video_link_to_markdown(video_id, title):
    sanitized_title = sanitize_filename(title)
    filename = f"VD-SM-{sanitized_title}.md"
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    os.makedirs(summary_files_path, exist_ok=True)
    
    template_path = os.path.join(templates_path, summary_template_file)
    template_content = read_template(template_path)
    
    filled_template = template_content.format(
        title=title,
        video_url=video_url
    )
    
    file_path = os.path.join(summary_files_path, filename)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(filled_template)
    
    print(f"Video link summary saved to {file_path}.")
import os
import re
from config import transcript_files_path, summary_files_path, templates_path, transcript_template_file, summary_template_file, merged_transcript_files_path

def save_transcript_to_markdown(video_id, transcript, title, language, include_timestamps=False):
    sanitized_title = sanitize_filename(title)
    filename = f"Tr-{sanitized_title}-{language}.md"
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    language_transcript_path = os.path.join(transcript_files_path, language)
    os.makedirs(language_transcript_path, exist_ok=True)
    
    template_path = os.path.join(templates_path, transcript_template_file)
    template_content = read_template(template_path)
    
    if not include_timestamps:
        transcript = transcript.replace('\n', ' ')
    
    filled_template = template_content.format(
        title=title,
        video_url=video_url,
        transcript=transcript,
        language=language
    )
    
    file_path = os.path.join(language_transcript_path, filename)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(filled_template)
    
    print(f"Transcript in {language} saved to {file_path}.")

def save_merged_transcript_to_markdown(video_id, merged_transcript, title, language1, language2, include_timestamps=False):
    sanitized_title = sanitize_filename(title)
    filename = f"Tr-{sanitized_title}-{language1}-{language2}.md"
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    os.makedirs(merged_transcript_files_path, exist_ok=True)
    
    template_path = os.path.join(templates_path, transcript_template_file)
    template_content = read_template(template_path)
    
    filled_template = template_content.format(
        title=f"{title} ({language1}/{language2})",
        video_url=video_url,
        transcript=merged_transcript,
        language=f"{language1}/{language2}"
    )
    
    file_path = os.path.join(merged_transcript_files_path, filename)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(filled_template)
    
    print(f"Merged transcript ({language1}/{language2}) saved to {file_path}.")

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
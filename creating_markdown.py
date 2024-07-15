import csv
import os
from config import transcript_files_path, summary_files_path, templates_path, transcript_template_file, summary_template_file

def sanitize_filename(filename):
    # Replace forbidden characters with an underscore
    forbidden_chars = '<>:"/\\|?*'
    for char in forbidden_chars:
        filename = filename.replace(char, '_')
    return filename

def read_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as template_file:
        return template_file.read()

def create_markdown_files(csv_file_path, limit=900):
    # Ensure the output directories exist
    os.makedirs(transcript_files_path, exist_ok=True)
    os.makedirs(summary_files_path, exist_ok=True)

    # Read templates
    transcript_template = read_template(os.path.join(templates_path, transcript_template_file))
    summary_template = read_template(os.path.join(templates_path, summary_template_file))

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)  # Convert iterator to list to count and reverse
        total_videos = min(limit, len(rows))  # Total videos to process, considering the limit

        for i, row in enumerate(rows[-total_videos:], 1):  # Start from the end if limiting
            video_number = total_videos - i + 1
            sanitized_title = sanitize_filename(row['Title'].replace(' - Computerphile', ''))
            
            # Create transcript file
            transcript_filename = f"SwiftUI-Tr-{video_number}-{sanitized_title}.md"
            transcript_file_path = os.path.join(transcript_files_path, transcript_filename)
            
            filled_transcript_template = transcript_template.format(
                title=row['Title'],
                video_url=row['Video URL'],
                transcript=row['Transcript'].replace('\\n', '\n') if row['Transcript'] != 'Transcript not available' else 'Transcript not available'
            )
            
            with open(transcript_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(filled_transcript_template)

            # Create summary file
            summary_filename = f"SwiftUI-SM-{video_number}-{sanitized_title}.md"
            summary_file_path = os.path.join(summary_files_path, summary_filename)
            
            filled_summary_template = summary_template.format(
                title=row['Title'],
                video_url=row['Video URL']
            )
            
            with open(summary_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(filled_summary_template)

    print(f'Markdown files have been created in the "{transcript_files_path}" and "{summary_files_path}" directories with a limit of {limit} files.')

# Example usage
csv_file_path = 'video_details.csv'  # Update this to the path of your CSV file
create_markdown_files(csv_file_path)
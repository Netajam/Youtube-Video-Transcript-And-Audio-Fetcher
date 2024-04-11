import csv
import os

def sanitize_filename(filename):
    # Replace forbidden characters with an underscore
    forbidden_chars = '<>:"/\\|?*'
    for char in forbidden_chars:
        filename = filename.replace(char, '_')
    return filename

def create_markdown_files(csv_file_path, output_directory='markdown_files', limit=900):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)  # Convert iterator to list to count and reverse
        total_videos = min(limit, len(rows))  # Total videos to process, considering the limit

        for i, row in enumerate(rows[-total_videos:], 1):  # Start from the end if limiting
            # Process the row
            #sanitized_title = sanitize_filename(row['Title'].replace(' - Computerphile', ''))
            # Calculate the numbering, starting from total_videos down to 1
            video_number = total_videos - i + 1
            ## Use sanitized_title if you want to sanitize the filename
            filename = f"SwiftUI-{video_number}-{filename}.md"
            file_path = os.path.join(output_directory, filename)

       """      with open(file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(row['Video URL'] + '\n\n')
                md_file.write('# Transcript\n\n')
                if row['Transcript'] != 'Transcript not available':
                    md_file.write(row['Transcript'].replace('\\n', '\n') + '\n')
                else:
                    md_file.write('Transcript not available\n') """

    print(f'Markdown files have been created in the "{output_directory}" directory with a limit of {limit} files.')

# Example usage
csv_file_path = 'video_details.csv'  # Update this to the path of your CSV file
create_markdown_files(csv_file_path)

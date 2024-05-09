import os

base_path = '/home/runner/work/TIL/TIL/MKDocs/docs'


def update_general_md(directory):
    md_files = [f for f in os.listdir(directory) if f.endswith('.md') and f != 'general.md']
    md_links = [f"* [{f.replace('.md', '')}]({f})" for f in md_files]
    content = f"# Table of Contents\n" + "\n".join(md_links)
    with open(os.path.join(directory, 'general.md'), 'w') as file:
        file.write(content)

categories = [os.path.join(base_path, d) for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

for category in categories:
    update_general_md(category)


# Run this command to update the general.md files with new links
# python update_general_pages.py

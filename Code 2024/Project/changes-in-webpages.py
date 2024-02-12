import os
import requests
import hashlib
import difflib

def download_html(url, output_folder):
    response = requests.get(url)
    if response.status_code == 200:
        page_name = url.split("/")[-1] if url.endswith("/") else url.split("/")[-1] + ".html"
        output_path = os.path.join(output_folder, page_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        return page_name
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")
        return None

def calculate_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def compare_html(previous_html, current_html):
    differ = difflib.HtmlDiff()
    diff = differ.make_file(previous_html.splitlines(), current_html.splitlines())

    # Filter out unchanged lines
    changed_lines = [line for line in diff.splitlines() if line.startswith('+ ') or line.startswith('- ')]
    return "\n".join(changed_lines)

def main():
    website_url = "https://brightbirdagency.com"
    output_folder = "html_pages"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Download current HTML
    current_page_name = download_html(website_url, output_folder)
    if current_page_name is None:
        return

    # Check if there is a previous version
    previous_page_path = os.path.join(output_folder, "previous_" + current_page_name)
    if os.path.exists(previous_page_path):
        # Read previous HTML
        with open(previous_page_path, "r", encoding="utf-8") as f:
            previous_html = f.read()

        # Read current HTML
        current_page_path = os.path.join(output_folder, current_page_name)
        with open(current_page_path, "r", encoding="utf-8") as f:
            current_html = f.read()

        # Compare HTML
        html_diff = compare_html(previous_html, current_html)

        # Output the differences
        if html_diff:
            print(f"Differences found in {current_page_name}:\n")
            print(html_diff)
        else:
            print(f"No differences found in {current_page_name}")

    # Save the current HTML as the previous version
    os.replace(os.path.join(output_folder, current_page_name), previous_page_path)

if __name__ == "__main__":
    main()
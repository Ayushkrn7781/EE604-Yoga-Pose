import os
import hashlib
import requests
from tqdm import tqdm

# Global counters
total_folders = 0
total_images = 0

# Function to check if an image exists and can be downloaded
def check_and_download_image(url, save_path):
    try:
        response = requests.get(url, stream=True, timeout=5)
        if response.status_code == 200:
            # Compute hash to avoid duplicates
            img_hash = hashlib.md5(response.content).hexdigest()
            file_path = os.path.join(save_path, f"{img_hash}.jpg")
            
            # Check if file with the same hash already exists
            if not os.path.exists(file_path):
                # Save image if hash not found
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                return True
        return False
    except requests.RequestException:
        return False

# Main function to process each .txt file in the folder
def download_images_from_text_files(folder_path):
    global total_folders, total_images

    # Iterate over all .txt files in the folder
    for txt_file in os.listdir(folder_path):
        if txt_file.endswith('.txt'):
            # Get the yoga pose name (filename without extension) and create a folder
            pose_name = os.path.splitext(txt_file)[0]
            pose_folder = os.path.join("../../../Main_Dataset", pose_name)
            os.makedirs(pose_folder, exist_ok=True)
            
            # Counter for successfully downloaded images for this folder
            successful_downloads = 0

            # Read URLs from the text file
            with open(os.path.join(folder_path, txt_file), 'r') as f:
                lines = f.readlines()
            
            # Process each line in the file
            for line in tqdm(lines, desc=f"Processing {pose_name}"):
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    file_name, url = parts
                    if check_and_download_image(url.strip(), pose_folder):
                        successful_downloads += 1
            
            # Update global counters
            total_folders += 1
            total_images += successful_downloads

            # Print summary for the current folder
            print(f"{pose_name}: {successful_downloads} images downloaded")

    # Print final summary
    print(f"\nTotal folders processed: {total_folders}")
    print(f"Total images downloaded: {total_images}")

# Run the function on the current folder
if __name__ == "__main__": # to run the script : $ python ./script.py
    folder_path = "."  # Current folder containing the .txt files
    download_images_from_text_files(folder_path)

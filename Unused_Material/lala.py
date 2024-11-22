import os
import zipfile

# Function to check if the source directory exists
def check_directory_exists(source_dir):
    if not os.path.isdir(source_dir):
        print(f"Error: The source directory {source_dir} does not exist.")
        return False
    return True

# Function to create the zip file and return the file object
def create_zip_file(output_zip):
    try:
        zipf = zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED)
        return zipf
    except Exception as e:
        print(f"Error creating zip file: {e}")
        return None

# Function to walk through the directory and collect files
def collect_files(source_dir):
    files_to_zip = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            files_to_zip.append(file_path)
    return files_to_zip

# Function to add files to the zip file
def add_files_to_zip(zipf, source_dir, files):
    try:
        for file_path in files:
            arcname = os.path.relpath(file_path, source_dir)
            zipf.write(file_path, arcname)
    except Exception as e:
        print(f"Error adding files to zip: {e}")

# Function to close the zip file
def close_zip_file(zipf):
    try:
        zipf.close()
    except Exception as e:
        print(f"Error closing zip file: {e}")

# Function to log the success message
def log_success(output_zip):
    print(f"Backup successful: {output_zip}")

# Main function to tie everything together
def zip_directory(source_dir, output_zip):
    if not check_directory_exists(source_dir):
        return

    zipf = create_zip_file(output_zip)
    if not zipf:
        return

    files_to_zip = collect_files(source_dir)
    add_files_to_zip(zipf, source_dir, files_to_zip)
    close_zip_file(zipf)
    log_success(output_zip)

if __name__ == "__main__":
    source_directory = input("Enter the directory to backup: ")
    output_zip = input("Enter the name of the output .zip file: ")

    if not output_zip.endswith('.zip'):
        output_zip += '.zip'

    zip_directory(source_directory, output_zip)

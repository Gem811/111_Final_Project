# Team member names
# Date
# CptS 111, Fall 2024
# Name of project
# Brief description and/or purpose of project; include sources
# Modules used

import os
import zipfile

def get_directory():
    """Ask the user for the directory to zip."""
    return input("Enter the directory to zip: ")

def list_files(directory):
    """List all files in the given directory."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def create_zip_filename(directory):
    """Create a zip filename based on the directory name."""
    return os.path.basename(os.path.normpath(directory)) + '.zip'

def name_zip_file():
    """Ask the user for the name of the output zip file."""
    zip_filename = input("Enter the name of the output .zip file: ")
    if not zip_filename.endswith('.zip'):
        zip_filename += '.zip'
    return zip_filename

def zip_files(files, zip_filename):
    """Zip all files into the given zip filename."""
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.relpath(file, os.path.dirname(files[0])))

def confirm_zip_creation(zip_filename):
    """Confirm that the zip file was created."""
    return os.path.exists(zip_filename)

def print_confirmation(zip_filename):
    """Print confirmation message."""
    print(f"Zip file '{zip_filename}' created successfully.")

def main():
    directory = get_directory()
    files = list_files(directory)
    zip_filename = name_zip_file()
    zip_files(files, zip_filename)
    if confirm_zip_creation(zip_filename):
        print_confirmation(zip_filename)
    else:
        print("Failed to create the zip file.")

main()
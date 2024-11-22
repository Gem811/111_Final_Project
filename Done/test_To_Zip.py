import unittest
import os
import zipfile
import subprocess
from Done.To_Zip import get_directory, list_files, create_zip_filename, name_zip_file, zip_files, confirm_zip_creation, print_confirmation
class TestToZip(unittest.TestCase):

    def setUp(self):
        # Setup a test directory and a test file
        self.test_dir = 'test_dir'
        self.test_file = 'test_dir/test_file.txt'
        self.output_zip = 'test_dir.zip'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        # Clean up the test directory and the output zip file after each test
        if os.path.exists(self.test_dir):
            for root, dirs, files in os.walk(self.test_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.test_dir)
        if os.path.exists(self.output_zip):
            os.remove(self.output_zip)

    def test_directory_creation(self):
        # Test if the directory is created and contains the test file
        self.assertTrue(os.path.exists(self.test_dir))
        self.assertTrue(os.path.exists(self.test_file))

    def test_zip_file_creation(self):
        # Test if the zip file is created
        subprocess.run(['python', 'to_zip.py'], input=f'{self.test_dir}\n{self.output_zip}\n', text=True)
        self.assertTrue(os.path.exists(self.output_zip))

    def test_zip_file_contents(self):
        # Test if the zip file contains the correct files
        subprocess.run(['python', 'to_zip.py'], input=f'{self.test_dir}\n{self.output_zip}\n', text=True)
        with zipfile.ZipFile(self.output_zip, 'r') as zipf:
            self.assertIn('test_file.txt', zipf.namelist())

    def test_custom_zip_filename(self):
        # Test if the user can specify a custom name for the zip file
        custom_zip = 'custom_name.zip'
        subprocess.run(['python', 'to_zip.py'], input=f'{self.test_dir}\n{custom_zip}\n', text=True)
        self.assertTrue(os.path.exists(custom_zip))
        if os.path.exists(custom_zip):
            os.remove(custom_zip)

    def test_confirmation_message(self):
        # Test if the confirmation message is printed correctly
        result = subprocess.run(['python', 'to_zip.py'], input=f'{self.test_dir}\n{self.output_zip}\n', text=True, capture_output=True)
        self.assertIn(f"Zip file '{self.output_zip}' created successfully.", result.stdout)

if __name__ == '__main__':
    unittest.main()
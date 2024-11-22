import unittest
import os
import zipfile
from Unused_Material.lala import check_directory_exists, create_zip_file, collect_files, add_files_to_zip, close_zip_file, log_success, zip_directory
from Unused_Material.zip_example import get_directory, list_files, create_zip_filename, zip_files, confirm_zip_creation, print_confirmation

# Test cases for lala.py
class TestLala(unittest.TestCase):

    def setUp(self):
        # Setup a test directory and a test file
        self.test_dir = 'test_dir'
        self.test_file = 'test_dir/test_file.txt'
        self.output_zip = 'test_output.zip'
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

    def test_check_directory_exists(self):
        # Test if the directory exists
        self.assertTrue(check_directory_exists(self.test_dir))
        self.assertFalse(check_directory_exists('non_existent_dir'))

    def test_create_zip_file(self):
        # Test creating a zip file
        zipf = create_zip_file(self.output_zip)
        self.assertIsInstance(zipf, zipfile.ZipFile)
        zipf.close()

    def test_add_files_to_zip(self):
        # Test adding files to the zip file
        zipf = create_zip_file(self.output_zip)
        files = collect_files(self.test_dir)
        add_files_to_zip(zipf, self.test_dir, files)
        zipf.close()
        with zipfile.ZipFile(self.output_zip, 'r') as zipf:
            self.assertIn('test_file.txt', zipf.namelist())

    def test_close_zip_file(self):
        # Test closing the zip file
        zipf = create_zip_file(self.output_zip)
        close_zip_file(zipf)
        self.assertTrue(zipf.fp is None)

    def test_zip_directory(self):
        # Test the entire zip directory process
        zip_directory(self.test_dir, self.output_zip)
        self.assertTrue(os.path.exists(self.output_zip))

# Test cases for zip_example.py
class TestZipExample(unittest.TestCase):

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

    def test_create_zip_filename(self):
        # Test creating a zip filename based on the directory name
        zip_filename = create_zip_filename(self.test_dir)
        self.assertEqual(zip_filename, 'test_dir.zip')

    def test_zip_files(self):
        # Test zipping files into the zip file
        files = list_files(self.test_dir)
        zip_files(files, self.output_zip)
        with zipfile.ZipFile(self.output_zip, 'r') as zipf:
            self.assertIn('test_file.txt', zipf.namelist())

    def test_confirm_zip_creation(self):
        # Test confirming the creation of the zip file
        files = list_files(self.test_dir)
        zip_files(files, self.output_zip)
        self.assertTrue(confirm_zip_creation(self.output_zip))

    def test_print_confirmation(self):
        # Test printing the confirmation message
        files = list_files(self.test_dir)
        zip_files(files, self.output_zip)
        self.assertTrue(confirm_zip_creation(self.output_zip))
        print_confirmation(self.output_zip)

if __name__ == '__main__':
    unittest.main()
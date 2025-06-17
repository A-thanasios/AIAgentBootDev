import os
import unittest


from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


'''class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_info_dot(self):
        print(os.listdir('calculator'))
        result = get_files_info("calculator", ".")
        print(result)

    def test_get_files_info_pkg(self):
        result = get_files_info("calculator", "pkg")
        print(result)

    def test_get_files_info_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)

    def test_get_files_info_parent(self):
        result = get_files_info("calculator", "../")
        print(result)

class TestGetFileContent(unittest.TestCase):
    def test_get_file_content_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)
    def test_get_file_content_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
    def test_get_file_content_error(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

class TestWriteFile(unittest.TestCase):
    def test_write_root(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_write_pkg(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_write_temp(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)'''

class TestRunPythonFile(unittest.TestCase):
    def test_run_main(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_run_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_run_error(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_run_error2(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)

if __name__ == "__main__":
    unittest.main()
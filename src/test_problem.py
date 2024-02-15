import unittest
from unittest.mock import Mock, patch
import io
import zipfile
from contextlib import contextmanager
from problem import validate_zip_structure, extract_and_process_files

@contextmanager
def mock_zip_file(files):

    with io.BytesIO() as bytes_io:
        with zipfile.ZipFile(bytes_io, 'w') as zip_obj:
            for file_path, content in files.items():
                zip_obj.writestr(file_path, content)
        bytes_io.seek(0)
        yield zipfile.ZipFile(bytes_io, 'r')

class TestGraderFuncsRevised(unittest.TestCase):
    def test_validate_zip_structure_with_required_structure_revised(self):
        files = {
            "problem_name/description.md": b"Description",
            "problem_name/metadata.json": b'{"title": "Test"}',
            "problem_name/testcases/input1.txt": b"input1",
            "problem_name/testcases/output1.txt": b"output1",
            "problem_name/testcases/input2.txt": b"input2",
            "problem_name/testcases/output2.txt": b"output2"
        }
        with mock_zip_file(files) as zip_obj:
            self.assertTrue(validate_zip_structure(zip_obj))


from unittest import TestCase, main
from engine import get_testcases, check_is_valid_python, run_code
import os 

class TestGetTestCases(TestCase):
    def setUp(self):
        pass 

    def test_get_testcase(self):
        path = "example_problem"
        tests = get_testcases(path)
        
        
        expected_input_output = [
            ("3 4", "7"),
            ("10 -7", "3")
        ]
        
        for (real_input, real_output), (expected_input, expected_output) in zip(tests, expected_input_output):
            self.assertEqual(real_input, expected_input)
            self.assertEqual(real_output, expected_output)

class TestCheckIsValidPython(TestCase):
    def setUp(self):
        pass 

    def test_true(self):
        code = "print('Hello world')"
        self.assertTrue(check_is_valid_python(code))

    def test_false(self):
        code = "if 3 > 4\n\tprint('hi')"
        self.assertFalse(check_is_valid_python(code))
            
class TestRunCode(TestCase):
    def setUp(self):
        self.correct_code = """file=open('input_file.txt', 'r')
a, b = map(int, file.readline().strip().split())
file.close()
file = open("output_file.txt", "w")
file.write(str(a + b))
file.close()
"""
        
        self.incorrect_code = """file=open('input_file.txt', 'r')
a, b = map(int, file.readline().strip().split())
file.close()
file = open("output_file.txt", "w")
file.write(str(a - b))
file.close()
"""
        self.buggy_code = """file=open('input_file.txt', 'r')
a, b = map(int, file2.readline().strip().split())
file.close()
file = open("output_file.txt", "w")
file.write(str(a + b))
file.close()
"""

        self.hello_world = "print('Hello world!')"
     
        self.problem_path = "example_problem"

    def tearDown(self) -> None:
        self.assertNotIn('input_file.txt', os.listdir())
        self.assertNotIn('output_file.txt', os.listdir())
        
    def test_AC(self):
        real_verdict = run_code(self.correct_code, self.problem_path)
        self.assertEqual(real_verdict, ["AC", "AC"])
            
    def test_WA(self):
        real_verdict = run_code(self.incorrect_code, self.problem_path)
        self.assertEqual(real_verdict, ["WA", "WA"])
        
    def test_RE(self):
        real_verdict = run_code(self.buggy_code, self.problem_path)
        self.assertEqual(real_verdict, ["RTE", "RTE"])
        
    def test_hello_world(self):
        real_verdict = run_code(self.hello_world, self.problem_path)
        self.assertEqual(real_verdict, ["RTE", "RTE"])
        

main()
    

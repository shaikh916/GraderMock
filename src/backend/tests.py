from unittest import TestCase, main
from engine import get_testcases, check_is_valid_python, run_code

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
        code = "printf('Hello world')"
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
        
        self.problem_path = "example_problem"
        
    def test_AC(self):
        real_verdict = run_code(self.correct_code, self.problem_path)
        print(real_verdict)
        self.assertEqual(real_verdict, "AC")
        # TODO: test that input_file.txt and output_file.txt do not exist
    
    def test_WA(self):
        real_verdict = run_code(self.incorrect_code, self.problem_path)
        self.assertEqual(real_verdict, "WA")
        # TODO: test that input_file.txt and output_file.txt do not exist

main()
    
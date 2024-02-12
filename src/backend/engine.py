import os

def get_testcases(problem_path: str):
    """
    A generator that yields the tuples (input, output)
    Params:
    ---
    problem_path (str): the relative path to the problem's directory
    """
    
    path = f"./assets/problems/{problem_path}/testcases"
    
    input_dict = {}
    output_dict = {}
    

    for d in os.listdir(path):
        
        with open(path + "/" + d, "r") as file:
            if d.startswith("output"):
                testcase_id = d[6:]
                output_dict[testcase_id] = file.read()
            elif d.startswith("input"):
                testcase_id = d[5:]
                input_dict[testcase_id] = file.read()
    
    testcases_ids = sorted(list(input_dict.keys()))
    
    for id in testcases_ids:
        yield input_dict[id], output_dict[id]

def check_is_valid_python(code: str):
    """
    returns True if it's valid Python code
    return False otherwise
    
    (FOR NOW this doesn't work if the actual code raises an NameError Exception)
    """
    try:
        eval(code)
    except Exception as err:
        if type(err) == NameError:
            return False 
        return True  
    return True 
    

def run_code(code : str, problem_path: str) -> str:
    """
    Params:
    ---
    code (str): the source code to evalute, in Python!
    problem_path (str): the relative path to the problem's directory
    return (Verdict): AC/MLE/RTE/TLE/CE
    """
    
    # check that the code is valid Python code
    if not check_is_valid_python(code):
        return "CE"
    
    verdicts = set()
    
    for input, output in get_testcases(problem_path):
        with open("input_file.txt", "w") as file:
            file.write(input)
        exec(code)
        with open("output_file.txt", "r") as file:
            if file.read() == output:
                verdicts.add("AC")
            else:
                verdicts.add("WA")
                
        # TODO: delete input_file.txt and output_file.txt
           
    if verdicts == {"AC"}:
        return "AC"
    
    if "WA" in verdicts:
        return "WA"

    if "TLE" in verdicts:
        return "TLE"
    
    if "MLE" in verdicts:
        return "MLE"
    
    return "RTE"
    
    
    
    
    
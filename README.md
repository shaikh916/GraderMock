# Grader

This project is a basic mock version of a testing system like DMOJ or Leetcode.

- Given a problem from the system, you can submit a code, and it will test it throughout a set of testcases.
    - Compare the expected output with your code's output and give you and verdict.


![DEMO](https://github.com/aniervs/GraderMock/assets/44501642/34700e4e-64ce-47b4-8ff7-10e1114524dd)

## Verdicts

- `AC`: Accepted, your code passed all testcases.
- `TLE`: Time limit excedeed, your code took too long to run in at least one testcase.
- `MLE`: Memory limit excedeed, your code took too much memory.
- `RTE`: Run Time Error, some Exception ocurred during the execution.
- `CE`: Compilation Error, your code has a syntax error.

## Instructions on how to replicate

### Installation

Clone the repository, create the virtual environment and install requirements.

```bash
git clone https://github.com/aniervs/GraderMock
cd GraderMock
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Run
Navigate to the project's root folder and just run the following in your terminal
```Python
streamlit run ./src/app.py
```

## Specifications

### Problem structure
Inside the folder `assets/`, there is the folder `problems/` that contains all problems.

Each problem is defined by a folder with its name (for e.g., `problems/alice_bob/`) that contains the following structure
```bash
❯ tree alice_bob
alice_bob
├── description.md
├── metadata.json
└── testcases
    ├── input1.txt
    ├── input2.txt
    ├── output1.txt
    └── output2.txt
```
- The `description.md` file contains the description in Markdown.
- The `metadata.json` file contains the memory limit (in MegaBytes) and the time limit (in miliseconds):
```Json
{
  "memory_limit": 256,
  "time_limit": 1000
}
```
- The `testcases/` folder contains the input and output testcases. For each testcase, a file `input<ID>.txt` and a file `output<ID>.txt`.

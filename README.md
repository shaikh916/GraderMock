# Grader

This project is a mock version of a testing system like DMOJ or Leagues of Code.

- Given a problem from the system, you can submit a code, and it will test it throughout a set of testcases.
    - Compare the expected output with your code's output and give you and verdict.

## Verdicts

- `AC`: Accepted, your code passed all testcase.
- `TLE`: Time limit excedeed, your code took too long to run in at least one testcase.
- `MLE`: Memory limit excedeed, your code took too much memory.
- `RTE`: Some Exception ocurred during the execution.
- `CE`: For compiled languages, this means your code didn't compile.

## Instructions on how to replicate


### Installation

1. Clone the repository.
```bash
git clone https://github.com/aniervs/GraderMock
```
2. Navigate to the repository's root folder.
```bash
cd grader
```
3. Create a virtual environment.
```bash
python3 -m venv venv
```
4. Activate the virtual environment
```bash
source ./venv/bin/activate
```
5. Install the requirements
```bash
pip install -r requirements.txt
```

### Run




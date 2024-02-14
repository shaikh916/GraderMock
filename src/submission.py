from datetime import datetime

class Submission:
    def __init__(self, source_code, verdicts):
        self.source_code = source_code
        self.time = datetime.now()
        self.verdicts = verdicts

submissions = []


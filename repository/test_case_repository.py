from models.testcase import TestCase

class TestCaseRepository:


    def __init__(self) -> None:
        self.test_cases : list

    def add(self, test_case : TestCase):
        self.test_cases.append(test_case)

    def get_all(self) -> list:
        return self.test_cases
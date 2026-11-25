from models.testcase import TestCase

class TestCaseRepository:


    def __init__(self) -> None:
        self._test_cases : list[TestCase] = []

    def add(self, test_case : TestCase) -> None:
        self._test_cases.append(test_case)

    def get_all(self) -> list[TestCase]:
        return self._test_cases.copy()
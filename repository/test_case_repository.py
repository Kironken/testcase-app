from models.testcase import TestCase

class TestCaseRepository:


    def __init__(self) -> None:
        self.__test_cases : list[TestCase] = []

    def add(self, test_case : TestCase):
        self.__test_cases.append(test_case)

    def get_all(self) -> list[TestCase]:
        return self.__test_cases.copy()
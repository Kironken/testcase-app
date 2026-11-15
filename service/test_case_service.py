from repository.test_case_repository import TestCaseRepository
from models.testcase import TestCase

class TestCaseService:
    def __init__(self) -> None:
        self.repository = TestCaseRepository()

    def register_test_case(self, title : str, description : str, expected_result : str): 
        new_test_case = TestCase(title, description, expected_result)
        self.repository.add(new_test_case)
from uuid import UUID

class Testcase:

    def __init__(self, ID: str, title: str, description: str, expected_result: str):
        self.id = UUID
        self.title = title
        self.description = description
        self.expected_result = expected_result
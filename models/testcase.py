from uuid import uuid4, UUID

class TestCase:

    def __init__(self, title: str, description: str, expected_result: str):
        self.id : UUID = uuid4()
        self.title : str = title
        self.description : str = description
        self.expected_result : str = expected_result
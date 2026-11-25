from service.test_case_service import TestCaseService


class TestCaseDialog:
    
    def __init__(self) -> None:
        self._service = TestCaseService()

    def show_menu(self):
        option1 = "1) Register Test Case"
        option2 = "2) Show Test Cases"
        option3 = "3) Quit"

        while True:
            print(f"{option1}\n{option2}\n{option3}")
            selection = input("Choose an option ")
            selection = selection.strip()

            match selection:
                case "1":
                    title = input("Enter Title: ")
                    description = input("Enter Description: ")
                    expected_result = input("Enter Expected Result: ")
                    self._service.register_test_case(title, description, expected_result)

                case "2":
                    test_cases_list = self._service.get_all_test_cases()
                    for case in test_cases_list:
                        print(f"Title: {case.title}")
                        print(f"Description: {case.description}")
                        print(f"Expected Result: {case.expected_result}")
                        print(case.id)
                        print("\n")

                    input("Press any key to continue")

                case "3":
                    return

                case _:
                    input("Invalid option, Try again!")


                    
from custom_exceptions import InvalidStudentDataError


class StudentManager:
    def __init__(self, filename):
        self.filename = filename

    def add_student(self, name, age):
        # validation logic
        if not name or not isinstance(age, int) or age <= 0:
            raise InvalidStudentDataError("Invalid name or age provided.")
        
        try:
            with open(self.filename, "a") as file:
                file.write(f"{name},{age}\n")
        except Exception as e:
            print(f"An error occurred while adding the student: {e}")
        else:
            print(f"Student {name} added successfully.")

    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()

                if not data:
                    print("No student records found")
                else:
                    print("\n--- Student Records ---")
                    for line in data:
                        name, age = line.strip().split(",")
                        print(f"Name: {name}, Age: {age}")
        except FileNotFoundError:
            print("File not found. try adding student first.")
        except Exception as e:
            print(f"An error occurred while reading the student records: {e}")


    def search_student(self, keyword):
        try:
            with open(self.filename, "r") as file:
                results = [line.strip() for line in file if keyword.lower() in line.lower()]
                if results:
                    print("\n--- Search Results ---")
                    for student in results:
                        print(student)
                else:
                    print(f"No matching student records found for '{keyword}'")
        except FileNotFoundError:
            print("File not found. try adding student first.")
        except Exception as e:
            print(f"An error occurred while searching for student records: {e}")
        finally:
            print("Search operation completed.")
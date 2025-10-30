from student_manager import StudentManager
from custom_exceptions import InvalidStudentDataError

manager = StudentManager("students.txt")

def menu():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ").strip()
            try:
                age = int(input("Enter student age: "))
                manager.add_student(name, age)
            except ValueError:
                print("Age must be a number.")
            except InvalidStudentDataError as e:
                print("Custom Error:", e)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            keyword = input("Enter search keyword: ")
            manager.search_student(keyword)

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Try again.")


# ✅ Make sure this part is present
if __name__ == "__main__":
    print("main.py is running...")  # Debug check
    menu()

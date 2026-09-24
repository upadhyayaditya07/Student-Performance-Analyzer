from student_manager import StudentManager
from reporting import display_all_students, display_statistics, display_subject_summary, display_top_performers

def menu():
    print("\n=== Student Performance Analyzer ===")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Class statistics")
    print("5. Sort by average")
    print("6. Subject-wise summary")
    print("7. Top performers")
    print("8. Exit")

def add_student_ui(manager):
    student_id = input("Student ID: ").strip()
    name = input("Name: ").strip()
    try:
        marks = {
            "Python": float(input("Python marks (0-100): ")),
            "Mathematics": float(input("Mathematics marks (0-100): ")),
            "Problem Solving": float(input("Problem Solving marks (0-100): "))
        }
        manager.add_student(student_id, name, marks)
        print("Student added successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")

def main():
    manager = StudentManager()
    print("Welcome to Student Performance Analyzer!")
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student_ui(manager)
        elif choice == "2":
            display_all_students(manager.students)
        elif choice == "3":
            sid = input("Enter Student ID: ").strip()
            student = manager.search_student(sid)
            print(student if student else "Student not found.")
        elif choice == "4":
            display_statistics(manager.students)
        elif choice == "5":
            display_all_students(manager.sort_by_average())
        elif choice == "6":
            display_subject_summary(manager.students)
        elif choice == "7":
            display_top_performers(manager.students)
        elif choice == "8":
            print("Thank you for using the analyzer.")
            break
        else:
            print("Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    main()

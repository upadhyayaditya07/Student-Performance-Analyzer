from analyzer import (
    add_student,
    display_students,
    search_student,
    calculate_class_statistics,
    sort_students_by_average,
    show_subject_summary,
    show_top_performers,
)


def print_menu():
    print("\n===== STUDENT PERFORMANCE ANALYZER =====")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Class statistics")
    print("5. Sort students by average")
    print("6. Subject-wise summary")
    print("7. Show top performers")
    print("8. Exit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            calculate_class_statistics(students)
        elif choice == "5":
            sort_students_by_average(students)
        elif choice == "6":
            show_subject_summary(students)
        elif choice == "7":
            show_top_performers(students)
        elif choice == "8":
            print("Thank you for using the Student Performance Analyzer.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()

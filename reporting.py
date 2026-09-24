from statistics import class_statistics, subject_statistics

def display_all_students(students):
    if not students:
        print("No student records available.")
        return
    print("\nID | Name | Average | Grade")
    print("-" * 45)
    for student in students:
        print(f"{student.student_id} | {student.name} | {student.average():.2f} | {student.grade()}")

def display_statistics(students):
    stats = class_statistics(students)
    print("\nClass Statistics")
    print(f"Students: {stats['count']}")
    print(f"Class average: {stats['average']:.2f}")
    if stats["highest"] is not None:
        print(f"Highest average: {stats['highest']:.2f}")
        print(f"Lowest average: {stats['lowest']:.2f}")

def display_subject_summary(students):
    data = subject_statistics(students)
    print("\nSubject-wise Summary")
    for subject, stats in data.items():
        print(f"{subject}: Avg={stats['average']:.2f}, "
              f"High={stats['highest']:.2f}, Low={stats['lowest']:.2f}")

def display_top_performers(students):
    if not students:
        print("No student records available.")
        return
    print("\nTop Performers")
    for rank, student in enumerate(sorted(students, key=lambda s: s.average(), reverse=True)[:3], 1):
        print(f"{rank}. {student.name} ({student.average():.2f})")

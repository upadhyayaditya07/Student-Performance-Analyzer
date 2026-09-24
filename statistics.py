def class_statistics(students):
    if not students:
        return {"count": 0, "average": 0, "highest": None, "lowest": None}

    averages = [student.average() for student in students]
    return {
        "count": len(students),
        "average": sum(averages) / len(averages),
        "highest": max(averages),
        "lowest": min(averages),
    }

def subject_statistics(students):
    if not students:
        return {}
    subjects = students[0].marks.keys()
    result = {}
    for subject in subjects:
        values = [student.marks[subject] for student in students]
        result[subject] = {
            "average": sum(values) / len(values),
            "highest": max(values),
            "lowest": min(values),
        }
    return result

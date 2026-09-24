import unittest
from student import Student
from student_manager import StudentManager

class TestStudentPerformanceAnalyzer(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()
        self.manager.add_student("S01", "Aarav", {
            "Python": 90, "Mathematics": 80, "Problem Solving": 85
        })
        self.manager.add_student("S02", "Diya", {
            "Python": 70, "Mathematics": 75, "Problem Solving": 80
        })

    def test_average(self):
        self.assertAlmostEqual(self.manager.students[0].average(), 85)

    def test_grade(self):
        self.assertEqual(self.manager.students[0].grade(), "A")

    def test_search(self):
        self.assertEqual(self.manager.search_student("S02").name, "Diya")

    def test_duplicate_id_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("S01", "Other", {
                "Python": 50, "Mathematics": 50, "Problem Solving": 50
            })

    def test_sorting(self):
        ordered = self.manager.sort_by_average()
        self.assertEqual(ordered[0].name, "Aarav")

if __name__ == "__main__":
    unittest.main()

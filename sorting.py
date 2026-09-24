def selection_sort_by_average(students):
    """Sort students by average in descending order using selection sort."""
    result = students.copy()
    n = len(result)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if result[j].average() > result[max_index].average():
                max_index = j
        result[i], result[max_index] = result[max_index], result[i]
    return result

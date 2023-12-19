def get_high_scorers(students):
    high_scorers = []
    for student, marks in students.items():
        average_mark = sum(marks) / len(marks)
        if average_mark >= 78:
            high_scorers.append(student)

    return high_scorers


# Example usage:
student_marks = {
    "Alice": [85, 90, 80],
    "Bob": [75, 82, 79],
    "Charlie": [92, 88, 91]
}

high_scorers = get_high_scorers(student_marks)

if high_scorers:
    formatted_output = "\n".join(
        [f"{student}: Average Mark = {sum(student_marks[student]) / len(student_marks[student]):.2f}" for student in
         high_scorers])
    print("High Scorers with Average Marks >= 78:")
    print(formatted_output)
else:
    print("No high scorers found.")
##################################################################
def get_high_scorers(students):
    return [student for student, marks in students.items() if sum(marks) / len(marks) >= 78]

# Example usage:
student_marks = {
    "Alice": [85, 90, 80],
    "Bob": [75, 82, 79],
    "Charlie": [92, 88, 91]
}

high_scorers = get_high_scorers(student_marks)

if high_scorers:
    print("High Scorers with Average Marks >= 78:")
    for student in high_scorers:
        average_mark = sum(student_marks[student]) / len(student_marks[student])
        print(f"{student}: Average Mark = {average_mark:.2f}")
else:
    print("No high scorers found.")

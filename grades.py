# Program to calculate Grades based on custom grading system (No Credits)

def get_grade_point(marks):
    """Return grade point and letter grade based on university scheme."""
    if 95 <= marks <= 100:
        return 10, "S+"
    elif 90 <= marks < 95:
        return 10, "S"
    elif 80 <= marks < 90:
        return 9, "A"
    elif 70 <= marks < 80:
        return 8, "B"
    elif 60 <= marks < 70:
        return 7, "C"
    elif 50 <= marks < 60:
        return 6, "D"
    elif 40 <= marks < 50:
        return 5, "E"
    else:
        return 0, "F"

# Input: number of subjects
n = int(input("Enter number of subjects: "))

subjects = []

for i in range(n):
    name = input(f"\nEnter subject {i+1} name: ")
    marks = int(input(f"Enter marks for {name} (out of 100): "))

    gp, grade = get_grade_point(marks)   # grade point & grade
    subjects.append((name, marks, grade, gp))

# Output
print("\n========== Results ==========")
for sub in subjects:
    print(f"Subject: {sub[0]}, Marks: {sub[1]}, Grade: {sub[2]}, Grade Point: {sub[3]}")

import matplotlib.pyplot as plt


student_names = [
    "Arun Kumar", "Priya Sharma", "Rahul Singh", "Ananya Patel",
    "Karan Mehta", "Sneha Iyer", "Aditya Nair", "Pooja Joshi",
    "Vikram Gupta", "Neha Verma", "Rohan Das", "Divya Reddy",
    "Amit Yadav", "Kavya Rao", "Sanjay Kumar", "Meera Nair",
    "Harish Patel", "Asha Singh", "Manoj Sharma", "Nisha Gupta",
    "Deepak Verma", "Swathi Reddy", "Ajay Kumar", "LavanyaRathinavel",
    "Rakesh Das", "Preethi Nair", "Suresh Patel", "Anjali Sharma",
    "Varun Gupta", "Keerthana Rao", "Gokul Raj", "Dharshini Devi",
    "Rathinavelavanya", "Praveen Kumar", "Janani Priya", "Aravind Raj",
    "Mohan Krishna", "Bhavya Sharma", "Kishore Kumar", "Nandhini Devi",
    "Vignesh Kumar", "Akash Gupta", "Harini Priya", "Yogesh Kumar",
    "Sathya Raj", "Abinaya Devi", "Balaji Kumar", "Monisha Rani",
    "Surya Prakash", "Hemalatha Devi"
]



students = []

for i in range(50):

    maths = 40 + ((i + 1) * 3) % 61
    science = 35 + ((i + 1) * 4) % 66
    english = 45 + ((i + 1) * 5) % 56

    total = maths + science + english
    average = round(total / 3, 2)

    # Grade Calculation
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "PASS"

    if average < 50:
        status = "PIP"

    students.append({
        "id": i + 1,
        "name": student_names[i],
        "maths": maths,
        "science": science,
        "english": english,
        "total": total,
        "average": average,
        "grade": grade,
        "status": status
    })


students.sort(key=lambda x: x["average"], reverse=True)

for rank, student in enumerate(students, start=1):
    student["rank"] = rank


print("=" * 130)
print(" " * 45 + "STUDENT MANAGEMENT SYSTEM")
print("=" * 130)

print(
    f"{'Rank':<6}"
    f"{'ID':<6}"
    f"{'Name':<20}"
    f"{'Maths':<8}"
    f"{'Science':<10}"
    f"{'English':<10}"
    f"{'Total':<8}"
    f"{'Average':<10}"
    f"{'Grade':<8}"
    f"{'Status':<10}"
)

print("-" * 130)

for student in students:

    print(
        f"{student['rank']:<6}"
        f"{student['id']:<6}"
        f"{student['name']:<20}"
        f"{student['maths']:<8}"
        f"{student['science']:<10}"
        f"{student['english']:<10}"
        f"{student['total']:<8}"
        f"{student['average']:<10}"
        f"{student['grade']:<8}"
        f"{student['status']:<10}"
    )


pass_count = len(
    [s for s in students if s["status"] == "PASS"]
)

pip_count = len(
    [s for s in students if s["status"] == "PIP"]
)

print("\n")
print("=" * 50)
print("CLASS SUMMARY")
print("=" * 50)

print(f"Total Students : {len(students)}")
print(f"Pass Students  : {pass_count}")
print(f"PIP Students   : {pip_count}")


names = [student["name"] for student in students]
averages = [student["average"] for student in students]
grades = [student["grade"] for student in students]

plt.figure(figsize=(20, 8))

bars = plt.bar(names, averages)

plt.title("Student Report Card")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.xticks(rotation=90)

for bar, grade in zip(bars, grades):

    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        grade,
        ha='center',
        fontsize=8
    )

plt.tight_layout()
plt.show()


grade_count = {
    "A+": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

for student in students:
    grade_count[student["grade"]] += 1

plt.figure(figsize=(8, 8))

plt.pie(
    grade_count.values(),
    labels=[
        f"{grade} ({count})"
        for grade, count in grade_count.items()
    ],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Grade Distribution")

plt.show()


plt.figure(figsize=(8, 8))

plt.pie(
    [pass_count, pip_count],
    labels=[
        f"PASS ({pass_count})",
        f"PIP ({pip_count})"
    ],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("PASS vs PIP Analysis")

plt.show()


plt.figure(figsize=(8, 6))

bars = plt.bar(
    ["PASS", "FAIL/PIP"],
    [pass_count, pip_count]
)

plt.title("Pass vs Fail Student Count")
plt.xlabel("Status")
plt.ylabel("Number of Students")

for bar in bars:

    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha='center',
        va='bottom',
        fontsize=12
    )

plt.show()


print("\n")
print("=" * 50)
print("STUDENTS REQUIRING PIP")
print("=" * 50)

for student in students:

    if student["status"] == "PIP":

        print(
            f"{student['name']} | "
            f"Average = {student['average']} | "
            f"Grade = {student['grade']}"
        )

print("\nProgram Completed Successfully.")
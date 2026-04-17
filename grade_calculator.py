def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep shining 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better 💪"
    elif marks >= 60:
        return "D", "Nice try! Work a bit harder 📚"
    else:
        return "F", "Don't give up! Try again 🚀"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Please enter marks between 0 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def main():
    print("🎓 Student Grade Calculator\n")

    name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT:")
    print(f"Student: {name}")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Run program
main()
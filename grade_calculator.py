name = input("What is your name? ")

grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))
grade3 = float(input("Enter your third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("Student:", name)
print("Average:", average)

if average >= 90:
    print("Letter Grade: A")
elif average >= 80:
    print("Letter Grade: B")
elif average >= 70:
    print("Letter Grade: C")
elif average >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")
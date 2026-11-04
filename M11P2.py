
# function section

def calculate_grades(exam_one, exam_two, exam_three):

    total_points = exam_one + exam_two + exam_three

    average_score = total_points / 3

    return total_points, average_score


# input section

last_name = input("Enter student last name: ")
exam_one = float(input("Enter first exam score: "))
exam_two = float(input("Enter second exam score: "))
exam_three = float(input("Enter third exam score: "))


# processing section

total_points, average_score = calculate_grades(exam_one, exam_two, exam_three)


# output section

print(f"Student Last Name: {last_name}")
print(f"Total Points: {total_points:.2f}")
print(f"Average Exam Score: {average_score:.2f}")


# function section

def calculate_average(score_one, score_two, score_three, handicap):

    total_score = score_one + score_two + score_three

    average_score = total_score / 3

    average_handicap = average_score + handicap

    return average_score, average_handicap


# input section

last_name = input("Enter bowler last name: ")
score_one = float(input("Enter first game score: "))
score_two = float(input("Enter second game score: "))
score_three = float(input("Enter third game score: "))
handicap = float(input("Enter handicap: "))


# processing section

average_score, average_handicap = calculate_average(score_one, score_two, score_three, handicap)


# output section

print(f"Bowler Last Name: {last_name}")
print(f"Average Score: {average_score:.2f}")
print(f"Average Score with Handicap: {average_handicap:.2f}")

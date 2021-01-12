scores = input("please Enter the highest score").split()

for score in range(0, len(scores)):
    scores[score] = int(scores[score])


highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

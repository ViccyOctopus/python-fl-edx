question1 = "hunor is going to get a 5 on the AP Calculus examination "
question2 = "viccy is a scholar "
questions = [str(question1), str(question2)]
points = 0

def wronganswer():
    print("wrong")

def rightanswer():
    print("correct")
    global points
    points += 1

answer1 = input(question1)
if answer1 == "yes":
    rightanswer()
else:
    wronganswer()

answer1 = input(question2)
if answer1 == "no":
    rightanswer()
else:
    wronganswer()

#post this, make a score counter

total_score=(points)
total_score1=str(points)

percent = (total_score*100)/2
percent_total = str(percent)

print("You got " + total_score1 + " questions right in this quiz, giving you a score of " + percent_total + "%")

question1 = "hunor is going to get a 5 on the AP Calculus examination "
question2 = "viccy is a scholar "
questions = [str(question1), str(question2)]
score = 0
score = int(score)
score1 =(score + 1)
score2 = (score1 + 1)

def wronganswer():
    print("wrong")

def rightanswer():
    print("correct")

answer1 = input(question1)
if answer1 == "yes":
    rightanswer()
    score1 =(score + 1)
else:
    wronganswer()

answer1 = input(question2)
if answer1 == "no":
    rightanswer()
    score2 = (score1 + 1)
else:
    wronganswer()

#post this, make a score counter

total_score=(score2)
total_score1=str(total_score)

percent = (total_score*100)/2
percent_total = str(percent)

print("You got " + total_score1 + " questions right in this quiz, giving you a score of " + percent_total + "%")












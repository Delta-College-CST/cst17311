# This program offers entry for quiz answers (a-e) and grades 
# the quiz.

# -------------------------------------------------------------------- #        

def isAnswerValid(answer):
    if answer in ["a", "b", "c", "d", "e"]:
        answerOK =  True
    else:
        answerOK =  False
    return answerOK

# -------------------------------------------------------------------- #        

quizkey = ["e", "c", "c","d", "a"]  # Quiz answer key
answers = []                        # Answer list - initially empty
numQuestions = len(quizkey)         # Capture number of quiz questions

# -------------------------------------------------------------------- #        

# Loop through all quiz questions.  Prompt user for one quiz answer at
# a time.  Validate the answer.  If OK, append to quiz list
for questionNum in range (0,numQuestions):
    newanswer = input("Answer for Question " + str(questionNum+1) + ": ")
    while (not isAnswerValid(newanswer)):
        print("Invalid response..")
        newanswer = input("Answer for Question " + str(questionNum+1) + ": ")
    answers.append(newanswer)

# Grade quiz using key
numberCorrect = 0
for questionNum in range (0,numQuestions):
    if quizkey[questionNum] == answers[questionNum]:
        numberCorrect += 1

# Report quiz summary and overall score
print("Quiz key:     " + str(quizkey))
print("Your answers: " + str(answers))
print("Score: ",numberCorrect,"correct out of",numQuestions)

# -------------------------------------------------------------------- #        


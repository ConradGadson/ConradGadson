print('Welcome to Conrad Quiz')
answer=input('Are you ready to play the Conrad Quiz ? (yes/no) :')
score=0
total_questions=4

if answer.lower()=='yes':
    answer=input('Question 1: What is Conrad's last name?
    if answer.lower()=='Gadson':
        score += 1
        print('YES!!! YOU ARE A GENIUS')
    else:
        print('WRONG ANSWER')


    answer=input('Question 2: Is Conrad a System Network Administrator?')
    if answer.lower()=='yes':
        score += 1
        print('YES! LETS GET TO THE NEXT QUESTION..')
    else:
        print('Wrong Answer LOL')

    answer=input('Question 3: VERRYYY HARD: If life give you lemons, make ______')
    if answer.lower()=='Lemonade':
        score += 1
        print('correct')
    else:
        print('WRONG ANSWER')

    answer=input('Question 4: What University did Conrad attend?')
    if answer.lower()=='FAU':
        score += 1
        print('correct')
    else:
        print('WRONG ANSWERR LOL')


print('Thank you for Playing the Conrad quiz, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Stay blessed!')

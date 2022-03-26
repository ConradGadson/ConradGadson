print('Welcome to Conrad Quiz')
answer=input('Are you ready to play the Conrad Quiz ? (yes/no) :')
score=0
total_questions=4

if answer.lower()=='yes':
    answer=input('Question 1: Finish the lyric: I never sleep, because sleep is the cousin of ______ ')
    if answer.lower()=='death':
        score += 1
        print('YES!!! YOU ARE A GENIUS')
    else:
        print('SIKE! WRONG ANSWER HAHA')


    answer=input('Question 2: Is Pop Smoke the king of NY?')
    if answer.lower()=='yes':
        score += 1
        print('YESyes! LETS GET TO THE NEXT QUESTION..')
    else:
        print('SIKE!! Wrong Answer LOL')

    answer=input('Question 3: VERRYYY HARD: If life give you lemons, make ______')
    if answer.lower()=='Lemonade':
        score += 1
        print('correct')
    else:
        print('SIKE!!! WRONG ANSWERR LOOLLL')

    answer=input('Question 4: SUPERRRR HARD!!: what must you pass to get through life?')
    if answer.lower()=='vibe check':
        score += 1
        print('correct')
    else:
        print('SIKE!!! WRONG ANSWERR LOOLLL')


print('Thank you for Playing the Conrad quiz, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Stay blessed!')
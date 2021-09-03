import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly wolo'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'No'
    elif answerNumber == 5:
        return 'aLL haiL, king of tHe woLo'
    elif answerNumber == 6:
        return 'moNk...i neeD a MoNK'
    elif answerNumber == 7:
        return 'mOnK pleAse'
    elif answerNumber == 8:
        return 'aiyooHHH'
    elif answerNumber == 9:
        return 'Wololo'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

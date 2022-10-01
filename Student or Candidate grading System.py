# Student/Candidate grading System

score = int(input('Overall score of student/candidate: '))
# grading will :
# >90 = A
# >80 = B
# >70 = C
# >60 = D
# <60 = F

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# if 60 <= score <=100 OR :
if score >= 60 and score <= 100:
    print('Pass, Congratulations')
elif score >= 100:
    print('Super Pass, Great job')
else:
    print('Fail, better luck next time')

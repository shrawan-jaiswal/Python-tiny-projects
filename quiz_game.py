print('Welcome to my Computer quiz!')
playing = input('Do you want to play? : ')

if playing.lower() != 'yes':
    quit()

print("lets Play")

score = 0

answer = input('What does CPU stands for?: ')
if answer == ('Central Processing Unit'):
    print('correct!')
    score += 1

else:
    print('Incorrect!  ')

answer = input('What does GPU stands for?: ')
if answer == ('Graphics Processing Unit'):
    print('correct!')
    score += 1

else:
    print('Incorrect!  ')

answer = input('What does RAM stands for?: ')
if answer == ('Random Access Memory'):
    print('correct!')
    score += 1

else:
    print('Incorrect!  ')

answer = input('What does MLA stands for?: ')
if answer == ('Machine Learning Algorithm'):
    print('correct!')
    score += 1

else:
    print('Incorrect!  ')

print('You got ' + str(score) + ' questions correct! ')    
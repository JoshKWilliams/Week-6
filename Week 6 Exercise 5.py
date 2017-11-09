count = 0
for i in range(5):
    import random
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)
    while True:
        guess = (input('What is' + str(num_1) + 'x' + str(num_2) + '? '))
        if int(guess) == num_1*num_2:
            print('Correct')
            count += 1
            break
        else:
            print('Wrong, try again')
            count += 1
totalattempts = count / 5
print(str('Your average attempts were: ' + str(totalattempts)))
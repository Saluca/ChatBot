
def greet(bot_name,location):
    print('I am {}! ' .format(bot_name))
    print('I am a farseer from {}! ' .format(location))


def remind_name():
    print('What\'s your name?.')
    name = input()
    print('What a great name you have, {} !'.format(name))


def guess_age():
    print('Let me guess your age.')
    print('Enter the remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) )
def count():
    print('Give me a number and I will count up to it!')

    num = int(input())
    current = 0
    while current <= num:
        print(current, '!')
        current = current + 1


def quiz():
    print("Let's test your general knowledge.")
    question = print('Which of these personifies sleep in Greek mythology?')
    option_1 = 'Deimos'
    option_2 = 'Thanatos'
    option_3 = 'Hypnos'
    option_4 = 'Moros'
    print('You have 4 options:\n1. Deimos\n2. Thanatos\n3. Hypnos\n4. Moros')
    correct = option_3
    # print(question)
    answer = input()
    while answer != correct:
        print('Please, try again.')
        answer = str(input())
    else:
        print('That\'s right!')



greet('Eldrad Ulthran', 'Craftworld Ulthwe')
remind_name()
guess_age()
count()
quiz()


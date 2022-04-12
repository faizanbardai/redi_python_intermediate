import logging
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='math_game.log',
                    level=logging.DEBUG, format=log_format)


# Ask the user for his/her username. Store it in a variable.
user_name = input('What is your name? ')

# Ask the user for the answer of a simple math operation. Example: What’s the result of “5x2”?
is_user_answer_a_number = False
while not is_user_answer_a_number:
    try:
        user_answer = int(input('What is 5x2? '))
        is_user_answer_a_number = True
    except ValueError:
        print('Please enter a valid number.')


if user_answer == 10:
    # If the user gives the correct answer:
    # Print a “Correct answer” message.
    print('Correct answer')
    # Log an INFO message that records the name of the user and the fact that a correct answer was given.
    logging.info(f'Correct answer by {user_name}: {user_answer}')
else:
    # If the user gives a wrong answer:
    # Print an “Incorrect answer” message.
    print('Wrong answer')
    # Log an ERROR message that records the name of the user and the answer given.
    logging.error(f'Wrong answer by {user_name}: {user_answer}')

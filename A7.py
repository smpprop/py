# Define custom exceptions
class TooHighException(Exception):
     pass
class TooLowException(Exception):
    pass
class CorrectException(Exception):
        pass


def guess_number():
    stored_number = 42

    while True:
        try:
            user_input = input("Enter your guess: ")
            guess = int(user_input)

            if guess > stored_number:
                raise TooHighException
            elif guess < stored_number:
                raise TooLowException
            else:
                raise CorrectException

        except TooHighException:
            print("Your guess is too high. Try again.")
        except TooLowException:
            print("Your guess is too low. Try again.")
        except CorrectException:
            print("Congratulations! You guessed the correct number!")
            break
        except ValueError:
            print("Please enter a valid integer.")


# Call the function guess_number()
guess_number()

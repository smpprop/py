class TooHighException(Exception):
    pass
class TooLowException(Exception):
    pass
class CorrectException(Exception):
    pass

def guess_number():
    stored_num = 42

    while True:
        try:
            user_input = int(input("Enter your guess:"))
        
            if user_input > stored_num:
                raise TooHighException
            elif user_input < stored_num:
                raise TooLowException
            else:
                raise CorrectException
        
        except TooLowException:
            print("Try high value")
        except TooHighException:
            print("Try low value")
        except CorrectException:
            print("Your guess is correct")
            break
        except ValueError:
            print("Input Vaid value!")

guess_number()

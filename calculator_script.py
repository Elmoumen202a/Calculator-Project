from calculator import Calculator

def calculator():
    # Create an instance of the Calculator class
    calc = Calculator()

    while True:
        print('Simple Calculator in Python!')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for subtraction')
        print('Enter \'m\' for multiplication')
        print('Enter \'d\' for division')
        print('Enter \'q\' to quit')

        # Get user input for operation selection
        choice = input('Selection: ')

        if choice == 'q':
            # Exit the loop if the user chooses to quit
            break

        try:
            # Get a number from the user for the selected operation
            num = float(input('Enter a number: '))
            if choice == 'a':
                # Perform addition operation
                calc.add(num)
            elif choice == 's':
                # Perform subtraction operation
                calc.subtract(num)
            elif choice == 'm':
                # Perform multiplication operation
                calc.multiply(num)
            elif choice == 'd':
                # Perform division operation
                calc.divide(num)
            else:
                # Notify the user of an invalid character
                print('Sorry, invalid character')
        except ValueError as e:
            # Handle ValueError (e.g., when attempting to divide by zero)
            print(f'Error: {e}')

        # Display the current result and total values entered
        print(f'Current result: {calc.get_result()} total inputs: {calc.get_values_entered()}')


if __name__ == '__main__':
    # Run the calculator function
    calculator()

def verify_card_number(card_number):
 #defining the function with card_number as the paramater
    sum_of_odd_digits = 0
    #defining a variable and setting it = 0
    card_number_reversed = card_number[::-1]
    #this defines a variable as the card number but reversed.
    #It equals the index range of the card number from 0 to the last index both of which are optional to put in the bracket index thingy.
    #Then uses the step of -1 so starting at the end and going backwards 1 index at a time
    odd_digits = card_number_reversed[::2]
    #defines a variable as the reversed card number but every other index starting from 0
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
        #using a for loop. Changes the string 'digit' into an integer so we can add it to 0 and then iterate down the list.
        #same as redefining sum_of_odd_digits = sum_of_odd_digits + int(digit)
        #so it's now defined as an integer. If i printed that, it would iterate every other digit starting at index 0
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    #these two lines do the same thing as the odd portion but now just for every other number starting at index 1
    for digit in even_digits:
        number = int(digit) * 2
        #for loop for every digit in the even_digits list, defines number.
        #number = the converted digit integer * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        #if statement. if the digit * 2 is greater or equal to 10
        #within if statement, if it's true, then number now equals the rounded down quotient of number / 10 and then summed to the remainder of number /10 using modulo % thingy.
        sum_of_even_digits += number
        #within for loop, 0 = number + 0, redefines the variable
        #whole loop iterates this: every even digit is multiplied by 2, if it's not 10 or bigger, return the same number.
            #if it is 10 or greater, then return the rounded down quotient summed to the remainder. It's now a new list of numbers.
    total = sum_of_odd_digits + sum_of_even_digits
    #defines a variable as the sum of both of those variables
    return total % 10 == 0
    #if total / 10 has a remainder of 0, return True, otherwise False. Turns it boolean.
def main():
    #defining the main function
    card_number = '4111-1111-4555-1142'
    #defining a variable = this string of numbers
    card_translation = str.maketrans({'-': '', ' ': ''})
    #defining a variable as translating a string so that dashes and spaces become empty, or nothing, not sure on correct verbage for empty string
    translated_card_number = card_number.translate(card_translation)
    #defining a variable as translating the card number using the previous lines translation rule
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')
    #if the function returns True, print VAILID!, if False, print INVALID!
main()
#call the main function
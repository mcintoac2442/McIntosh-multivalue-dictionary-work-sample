'''
This module creates a MultiValueDictionary object for a user, and allows them to interact with it
via simple prompts and function calls. Appropriate messages are displayed to the user when input
does not match what is expected.

Functions:

    UNRECOGNIZED(*_)
    EXIT()
'''

import multivalue_dict

def UNRECOGNIZED(*_):
    '''
    Prints an error message to the user, notifying them the function name used was not recognized.

    Default function call for unrecognized function names from user input.

    Parameters
    ----------
        *_: Infinite unused parameters to account for misc. user input
    
    Returns
    -------
        None
    '''
    print("ERROR, function name not recognized. Please try again!\n")
    return

def EXIT():
    '''
    Ends the program.

    Parameters
    ----------
        None

    Returns
    -------
        None
    '''
    quit()

# Created by Anthony McIntosh, 6/4/2021
def main():
    '''
    Continusouly prompts the user for input to interact with a MultiValueDictionary object.

    Creates a MultiValueDictionary object for the user. Continuously parses user input and
    compares it to keys within function_name_switcher. This either calls the appropriate function
    prompted by the user, or prints an appropriate error message.

    Parameters
    ----------
        None

    Returns
    -------
        None
    '''
    myDictionary = multivalue_dict.MultiValueDictionary()

    function_name_switcher = { #Originally used to easily parse user input and call the appropriate function
        "KEYS": myDictionary.KEYS,
        "MEMBERS": myDictionary.MEMBERS,
        "ADD": myDictionary.ADD,
        "ADDMANY": myDictionary.ADDMANY,
        "REMOVE": myDictionary.REMOVE,
        "REMOVEALL": myDictionary.REMOVEALL,
        "CLEAR": myDictionary.CLEAR,
        "KEYEXISTS": myDictionary.KEYEXISTS,
        "MEMBEREXISTS": myDictionary.MEMBEREXISTS,
        "ALLMEMBERS": myDictionary.ALLMEMBERS,
        "ITEMS": myDictionary.ITEMS,
        "EXIT": EXIT
    }

    print("Your multivalue dictionary has been created! Type the expected inputs to interact with it.\n")
    print("Your options are: \nKEYS\nMEMBERS\nADD\nADDMANY\nREMOVE\nREMOVEALL\nCLEAR\nKEYEXISTS\nMEMBEREXISTS\nALLMEMBERS\nITEMS\n")
    print("Type EXIT to end the program.")
    print("=======================================================\n")

    # Continuously reads user input and calls the appropriate function.
    # Errors/Edge cases caught include no input, incorrect function call, and incorrect # of arguments.
    while True:
        user_input = input("> ")
        split_input = user_input.split() #Default split is space
        if len(split_input) == 0:
            print("ERROR reading input, no strings detected! Please try again.\n")
        else:
            function_call, *function_arguments = split_input #function_arguments will be a list (potentially empty)
            try:
                # Original Method
                # function_name_switcher.get(function_call, UNRECOGNIZED)(*function_arguments)

                # Scalable Method
                if function_call == "EXIT": 
                    EXIT()
                else:
                    getattr(myDictionary, function_call, UNRECOGNIZED)(*function_arguments)
                    # If you had lots of possible local module functions that could be called, I would make the default return a helper function
                    # that then runs locals().get(function_call, UNRECOGNIZED)(#function_arguments) to see if the function exists within this module.
            except(TypeError):
                print("ERROR, incorrect number of arguments! Please try again.")

if __name__ == "__main__":
    main()
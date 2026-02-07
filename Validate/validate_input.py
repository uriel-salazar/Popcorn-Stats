
def verify_number(answer):
    """ Verify if it's a valid number
    If not, is going to ask the question again 

    Args:
        answer (int) User's input 


    Returns:
        int:  User's input validated 
    """
    while True:
        user_input = input(answer).strip()  
        try:
            num = int(user_input)
            
        except ValueError:
            print("Please enter a valid number")
            continue
        return num


def get_letters(prompt):
    """
    Forces user to enter only letters without spaces.

    Args:
        prompt (str): message shown to the user

    Returns:
        str: Validated text containing only letters and spaces
    """
    
    while True:
        text = input(prompt).strip()
        
        if all(word.isalpha() for word in text.split()):
            return text
        else:
            print("❌ Only letters allowed. Please try again.")
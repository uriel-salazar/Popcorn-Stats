
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
    
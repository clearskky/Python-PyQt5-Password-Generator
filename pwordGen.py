import random

def pwordGenn(digit):
	
        letters = ['q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        characters = ['#','$','&']
	
        password = []
	
        for i in range(int(digit)):
                p_choices = [1,2,3,4,5,6,7]
                choice = random.choice(p_choices)
		
                if choice in [1,2,3]:
                        password.append(random.choice(letters)) # 3/7 chance for each character in a password to be a letter.
                elif choice in [4,5,6]:
                        password.append(random.choice(numbers)) # 3/7 chance for each character in a password to be a number.
                else:
                        password.append(random.choice(characters)) # 1/7 chance for a special character. I did it this way because I didn't like it when there were too many special symbols in a password.
        result = "".join(password) # This line creates a single string out of all the elements in an iterable.
        return result

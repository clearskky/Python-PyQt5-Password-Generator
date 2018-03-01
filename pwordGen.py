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
                        password.append(random.choice(letters))
                elif choice in [4,5,6]:
                        password.append(random.choice(numbers))
                else:
                        password.append(random.choice(characters))
        result = "".join(password)
        return result
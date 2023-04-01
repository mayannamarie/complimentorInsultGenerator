import random
import re

compliment = ["special", "kind", "enough",
            "beautiful", "incredible", "wonderful"]
insult = ['silly', 'stupid', 'ass-kisser',
        'bastard', 'rat', 'pig', 'asshole', 'jerk','deadbeat']

def GetCompliment_OrInsult():
    name = input(str('Enter your name here: '))
    #regex
    validateName = re.search("^([A-Za-z])\w+$", name)
    randomCompliment = 'Hey ' + name + ', be sure to remember that you are ' + \
        random.choice(compliment) + ' and ' + random.choice(compliment) + '.'

    randomInsult = 'I need to get something off my chest, you are a ' + \
        random.choice(insult) + ', ' + random.choice(insult) + \
        ' and a ' + random.choice(insult) + ' on your best day.'

    # if validateName is none or false, so the user input doesnt pass validation
    if not validateName or not name:
        print('You entered an INVALID name, please try again.')
        GetCompliment_OrInsult()
        return 

    while True:
        responseType = input(f"Hi, {name}! Would you like a compliment or an insult today? ")
        #lowercases input, strip removes tailing or leading spaces
        responseType = responseType.lower().strip()        
        if responseType == str('compliment'):
            print(randomCompliment)
            return
        elif responseType == str('insult'):
            print(randomInsult)
            return
        else:
            print('You entered an incorrect response, please try again.')

GetCompliment_OrInsult()
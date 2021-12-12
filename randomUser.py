import random, string

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def random_id() -> str:
    idSet = set()
    while (len(idSet) < 5):
        idSet.add(str(random.randint(0, 9)))
    
    return ''.join(idSet)
    
def random_login() -> str:
    letters = string.ascii_lowercase
    lst = [random.choice(letters) for i in range(5)]
    
    notVowel = random.choice(letters)
    while (notVowel in vowels):
        notVowel = random.choice(letters)
        
    lst.append(notVowel)
    return ''.join(lst)
    
def random_password() -> str:
    bigLetters = string.ascii_uppercase
    smallLetters = string.ascii_lowercase
    passwordSet = set()
    smallBig = True
    
    while (len(passwordSet) < 6):
        if (smallBig):
            passwordSet.add(random.choice(smallLetters))
            smallBig = False
        else:
            passwordSet.add(random.choice(bigLetters))
            smallBig = True
            
    digSet = set()
    
    while (len(digSet) < 3):
        digSet.add(str(random.randint(0, 9)))
        
    vowel = random.choice(vowels)
    while (vowel in passwordSet):
        vowel = random.choice(vowels)
        
    return ''.join(passwordSet) + ''.join(digSet) + vowel
    
def user_generator(n : int):
    for i in range(0, n):
        print(random_id(), end=" ")
        print(random_login(), end=" ")
        print(random_password())
        
user_generator(5)

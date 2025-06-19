# Create random passwords using letters, numbers, and symbols. use the random and using string modules.

# string.ascii_lowercase  ->	'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase  -> 	'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters  -> 	'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.digits  ->	'0123456789'
# string.punctuation  ->	Special symbols like !"#$%&'() etc.
# string.whitespace  ->	Space, tab, newline, etc.

import string
import random
import math

# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(characters) for i in range(10))
# print(password)



def names(name):
    if name:
        ...
    else:
        name = False
    
    return name

symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '/', '?', '<', '>', '|', ':']
alphabetSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetBig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
listOfAll = [symbols, numbers, alphabetBig, alphabetSmall]

def createPass(listCount, NameList):
    finalName = ''; count = 1
    for j in NameList: finalName += j

    for k in listCount:
        if k == 0: count += 1

    newCount = 0
    for i in listCount:
        if i == 0:
            checkOutList = listOfAll[newCount]
            if len(finalName) < 13:
                for runTime in range(count):
                    finalName += checkOutList[random.randint(0, len(checkOutList) - 1)]
        newCount += 1
    return finalName

def checkStrings(userName):
    listOfExist = []
    if not userName:
        userName = ''; userName += alphabetBig[random.randint(0, len(alphabetBig) -1)]
        for k in range(8):
            userName += alphabetSmall[random.randint(0, len(alphabetSmall) - 1)]

    nameList = [i for i in userName]; nameList[0] = nameList[0].title()

    for j in listOfAll:
        count = 0
        for k in j:
            if k in nameList: count += 1
        listOfExist.append(count)
    
    return createPass(listCount=listOfExist, NameList=nameList)

def PassGen(name = ''):
    userName = names(name=name)
    processName = checkStrings(userName=userName)
    return processName

print(PassGen(name='suresh'))
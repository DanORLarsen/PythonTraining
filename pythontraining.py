print("Hello World")

def say(text):
    print(text)

say("Hello World - Method")

def returnSay(text):
        return "Return - " + text #Easy to concatenate

print(returnSay("Hello world - Return"))


def multipleSay(text, amount):
    i = 0
    while i < amount:
        #input("Get Message") #Can be used to request data from the user. just like Scanner in java. but more flexible(waits for enter)
        print(text)
        i += 1
        
#To limit input to only int u could do this 
def getNumberFromInput(number):
    d = (input('Give a number')) #invalid option???
    print(d)

multipleSay("hey", 5)


def oddOrEven(number):
    if (number % 2) is 0:
        print("{} is Even".format(number)) #Usefull to add numbers and other specific vars into text. 
    elif number % 2 is 1:
        print("{} is odd{}".format(number, "."))#.format allows you to insert var in text. using {}, if more than one, it will add them in order of input in format.

oddOrEven(1231)

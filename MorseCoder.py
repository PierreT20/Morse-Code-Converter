#Here is the main function that takes the use of all other functions and puts them to work all together
def main():
    MorseDict = {}
    MorseDict = dictionary(MorseDict)
    message = ' '
    #Right here we have a little while loop that helps repeat the and end the program depending on the input chosed by the operator
    while True:
        choice = Menu()
        if choice == 't':
            text = input("\nPlease enter text to translate:\n")
            morseCode = encryption(text.upper(),MorseDict)
            print(morseCode)
            print()#did this to make more space
        elif choice == 'm':
            morseCode = input("\nPlease enter morse to translate:\n")
            text = decryption(morseCode.upper(),MorseDict)
            print(text)
            print()#did this to make more space
            
        elif choice == 'e':
            print("\nThanks for using this program.\n")
            break
#Here is a function specifically made to open the file split he collums and make a dictionary that you will be able to use by passing through its name (MorseDict)
def dictionary(MorseDict):
    MorseDict = {}
    MorseFile = open('MorseCode.txt','r')
    for line in MorseFile:
        key, value = line.split()
        MorseDict[key] = value
    return MorseDict
#Here is the first important function its entire purpose is to change normal english wrting to morse code.
#We pass through message and the dictionary to be able to take variable and information from the dictionary and replace the letter to the equivalent morese code
def encryption(message,MorseDict):
    encrypt = ''
    for letter in message:
        if letter !=' ':
            #Here is where it really looks the at the dictionary and what each letter is in order to replace them with the morse code equivilance and make a space between each character
            encrypt = encrypt + MorseDict[letter] + ' '
        #Here i used to to make spaces bewtween each actual word
        else:
            encrypt = encrypt + '   '
    return encrypt
#This function here is to do the complete opposite of the encrypt function.
def decryption(message,MorseDict):
    #We add a space here to be able to read the las morse code
    message += ' '
    decrypt = ''
    EncrpytedText= ''
    #in this for loop I am using it to be able to count the white spaces, here if the character is not an empty space i stays zero but once it is not a white space it gets 1 added to it so when I is atleast 2 characters it know its a word and is then asked to make a 3 character space before writing the next word.
    for letter in message:
        if letter !=' ':
            i = 0
            EncrpytedText = EncrpytedText + letter 
        else:
            i = i + 1
        #Here it is supposed to make a space between each word
            if i >= 2: 
                decrypt =  decrypt + ' '
            else:
                #Right here this long line is used to access the the dictionary and match the values with there keys in this case the keys being the letters and the morse code being its values.
                decrypt = decrypt + list(MorseDict.keys())[list(MorseDict.values()).index(EncrpytedText)]
                EncrpytedText = ''
    return decrypt
#This function here is specificalle made to make the menu, printing the greeting for the operator and asking for the user input
def Menu():
    print("Hello, this program allows you to translate text to morse code or translate morse code to text")
    print()
    print("Please, select one of the below options:")
    print()
    print("*** Enter 't' for encoding text")
    print("*** Enter 'm' for decoding morse code")
    print("*** Enter 'e' to exit the program.")

    choice = input("\nMy input is: ")
#Here I made a while loop so if the user enters an invald input it makes them input a different character and keeps going until one has been given
    while True:
        if choice == 't' or choice == 'e' or choice == 'm':
            return choice
        else:
            print('***invalid option***')
            choice = input('Please enter a valid option: ')

main()


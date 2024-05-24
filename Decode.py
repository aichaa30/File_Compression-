from Code import loadSheet  # gets our excel loading function from other file
table = {}

# checkChar reads the binary output and checks the table for corresponding char. Writes text to a new text file
def Decode(filename="BinOutput.txt"):
    table = loadSheet(False)
    file = open(filename)
    output = open("TextOutput.txt", 'w+')
    textString = ""
    character = file.read()
    var = character.index(".") + 1
    while var < len(character):  # while loop iterates over the binary string and checks the table and adds value to a new string
        if character[var] == "0":  # checks if binary value is short
            textString += (table[character[var: var+5]])
            var += 5
        elif character[var] == "1":  # checks if long
            if character[var: var+7] == "1110111":  # special case for a specific variable, new line.
                textString += "\n"
                var += 7
            else:
                textString += (table[character[var: var+7]])
                var += 7
    output.write(textString)

Decode()
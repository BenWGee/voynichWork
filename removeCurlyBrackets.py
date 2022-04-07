"""
@overview: Delete all curly brackets, and the text in between them
"""

import re

def dropCurlyBrackets(input, output):
    text = open(input, 'r').read()
    textModified= re.sub("{.*}", "", text)

    #open text file
    textFile = open(output, "w")

    #write string to file
    textFile.write(textModified)

    #close file
    textFile.close()

input = "" #name of file to read in (include the file extension)
output = "" #name to save output as (include the file extension)

fileNames = ["","","","","",""]
filesOut = [f + "output.txt" for f in fileNames]
filesIn = [f + ".txt" for f in filesIn]
for f in files
    dropCurlyBrackets(input, output)

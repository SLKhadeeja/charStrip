import re

def strip(text, char):
    defaultRegex = re.compile(r'(^\s)?(\s$)?')
    charRegex = re.compile(char)

    if char != '':
        text = charRegex.sub('', text)
    elif char == '':
        text = defaultRegex.sub('', text)

    print(text)  

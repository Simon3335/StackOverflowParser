import re

__doc__ = "Library to parse html code and convert them to their equivalent ascii values."

__all__ = ['char', 'replace']

def char(character):
    ''' Convert html character to ascii equivalent '''
    return bytes(chr(int(character.strip(b'&#')[:-1])), 'utf-8')

def replace(string):
    ''' replace all html characters by their ascii equivalent '''
    regex = re.compile(rb'&#\d+;')
    
    for character in regex.findall(string):
        string = string.replace(character, char(character))

    return string




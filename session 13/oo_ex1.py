import wordlist
import os

def createReader(filename):
    file_name,file_ext=os.path.splitext(filename)
    if (file_ext==".json"):
        return wordlist.JsonFileWordList(filename)
    else:
        return wordlist.CsvFileWordList(filename)
    
textwords=createReader("..\\session 11\\target_words.txt")
jsonwords=createReader("words.json")

assert textwords.has_word("abled")
assert jsonwords.has_word("abled")

jsonwords = createReader("words.json")

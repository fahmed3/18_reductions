file = open("themanoutside.txt", "r")
text = file.read()
file.close()

punctuations = '''!()-[]{};:"\,<>./?@#$%^&*_~'''

no_punct = ""
for char in text:
   if char not in punctuations:
       no_punct = no_punct + char

#print no_punct
story = no_punct.split()
#print story

def frequency(word):
    return len([x for x in story if x.lower() == word.lower()])

print "Frequency of the word 'the':", frequency("the") #7487

def totalFreq(words):
    return reduce(lambda a,b: frequency(b)+frequency(a), words)

print "Frequency of the words ['the','father']:", totalFreq(['the','father']) #should 7494

def mostFreq():
    return reduce(lambda a,b: a if frequency(a) > frequency(b) else b, story)

print "Most frequent word: ", mostFreq()


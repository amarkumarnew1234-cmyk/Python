'''6. Program to count number of unique words in a given sentence using sets. '''
'''sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
'''
sentence=input("Enter the sentence:")
words=sentence.split()
unique_words=set()
for word in words:
    unique_words.add(word.lower())
print("Number of unique words:",len(unique_words))

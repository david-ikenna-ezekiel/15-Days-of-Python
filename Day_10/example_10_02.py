# Word Count

def word_count(s):
    words = s.split()
    return len(words)

sentence = input("Enter a sentence: ")
print("Number of words:", word_count(sentence))
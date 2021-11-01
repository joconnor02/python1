def user_input():
    words = input("Please input a sentence")
    return words

def split1(words):
    new_word = ""
    for word in words:
       if word == " ":
            print(new_word)
            new_word = ""
       else:
           new_word += word
    print(new_word)

def split2(words):
    wordstogether = words.split(' ')
    for word in wordstogether:
        print(word)

sentence = user_input()
print(split1(sentence))
print(split2(sentence))

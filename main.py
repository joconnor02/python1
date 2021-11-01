def piggy(word):
    first = word[0].lower()
    second = word[1]
    if first in ['a', 'e', 'i', 'o', 'u', 'y']:
        word += "yay"
        return word
    if second in ['r', 'h']:
        return word[2:] + first + second + "ay"
    else:
        return word[1:] + first + "ay"
#How do you detect consonant clusters?
def user_input():
    words = input("Please input a sentence")
    return words

sent = user_input()
words = sent.split(' ')
new_sent = ""
for word in words:
    new_sent += piggy(word) + " "
print(new_sent)

# import re

# def highlight_word(sentence, word):

#     sentence = re.findall(r"[\w']+|[.,!?;]", sentence)
#     for index, a_word in enumerate(sentence):
#         if a_word == word:
#             sentence[index] = sentence[index].upper()

#     return " ".join(sentence)
# This method not working for that stupid punctuation


def highlight_word(sentence, word):

	index = sentence.find(word)
	new_text = sentence[:index] + sentence[index:index + len(word)].upper() + sentence[index + len(word):]
	return new_text


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

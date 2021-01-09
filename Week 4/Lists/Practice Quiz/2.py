def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  pig_words = list()
  for word in words:
    # Create the pig latin word and add it to the list
    pig_words.append(word[1:] + word[0] + 'ay')
    # print(word)
    # Turn the list back into a phrase
  return " ".join(pig_words)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
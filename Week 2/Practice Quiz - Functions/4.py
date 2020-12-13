def lucky_number(name):
  number = len(name) * 9
  msg_to_return = "Hello " + name + ". Your lucky number is " + str(number)
  return msg_to_return
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

def format_address(address_string):
  # Declare variables
  house_number = ""
  street = ""
  # Separate the address string into parts
  house_number = address_string.split()[0]
  street = " ".join(address_string.split()[1:])
  # Traverse through the address parts
  # for __:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

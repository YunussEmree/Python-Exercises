word = input("Type your messages : ")
shiftnumber = int(input("Type the shift number : "))


encoded_list = list(word.upper().encode('ascii'))
print(encoded_list)
new_encoded_list = " "

for number in encoded_list :
  number += shiftnumber
  if(shiftnumber > 132) : shiftnumber -= 32
  new_encoded_list += (chr(number))
  
print(new_encoded_list)

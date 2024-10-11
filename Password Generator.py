import random

letters = input("How many letters would you like in your password? : ")
symbols = input("How many symbols would you like in your password? : ")
numbers = input("How many numbers would you like in your password? : ")


let = "abcçdefgğhıijklmnoöprqsştuüvwyz"
sym = "$%&/()=?*+-:;.,<>\|!#^~@[]`~"
num = "0123456789"

password = []

for i in range(int(letters)):
    password.append(random.choice(let))

for j in range(int(numbers)):
    password.append(random.choice(num))

for k in range(int(symbols)):
    password.append(random.choice(sym))


print(password)

passcode = random.sample(password, len(password))
print(passcode)

shuffledpassword = "".join(passcode)


print("Here is your password : " + str(shuffledpassword))
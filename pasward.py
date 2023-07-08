#paswaord genratpr 
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
'r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','*','(',')','+']
print("Welcome to the pasward genrator!")
nr_letters=int(input("how many letter would you like in a paswaward "))
nr_number=int(input("how many number would you like in your passward "))
nr_symbol=int(input("how many symbol would you like in your passward "))
pasward=""
for char in range (1,nr_letters+1):
    pasward+=random.choice(letter)
for no in range (1,nr_number+1):
  pasward+=random.choice(number)
for sym in range (1,nr_symbol+1):
    pasward+=random.choice(symbols)

print(pasward)
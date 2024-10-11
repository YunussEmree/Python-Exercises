bids = dict()

def new_bid(dic) :
  name = input("Type your name : ")
  bid_price = int(input("Type your bid : "))
  bids[name] = bid_price


while True :
  
  new_bid(bids)
  
  if input("new bid ? : ") == "False" : break



max_bid = 0
who = ""

for name in bids :
  bid = bids[name]
  if bid > max_bid : 
    max_bid = bid
    who = name

print(f"The winner is {who} with " + str(max_bid))
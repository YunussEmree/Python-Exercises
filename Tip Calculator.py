print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? : ")
tip = input("How much tip would you like to give? : ")
split_people = input("How many people to split the bill? : ")

cost_for_each_people = (float(total_bill) + float(tip)) / float(split_people)
print(round(cost_for_each_people , 2))
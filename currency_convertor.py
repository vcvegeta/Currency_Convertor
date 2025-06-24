with open("currency_rates.txt","r") as f:       # open() returns a file object which lets you interact with the file in read mode
    lines= f.readlines()                        # gives out a list which has each line string one by one separated by commas 

# print(lines)
print()

currency_dict={}                                # empty dictionary
for line in lines:
    parsed=line.split("\t")                     # parsed has the returned list
    currency_dict[parsed[0]]=parsed[1]          # creating a key value pair inside the empty dicitionary ie currency_dict
    # print(parsed)
print(currency_dict)                            #  parsing data smartly to a dictionary (mutable) on which operations can be performed now

amount =int(input("Enter the amount you wanted to convert: "))

print(f"Enter the currency you want to convert your amount {amount} to: Available currency options are given below:\n")

# for each_key in currency_dict.keys():
#     print(each_key)

[print(each_key) for each_key in currency_dict.keys()]          # list comprehension is used as an alternative here 

currency_chosen= input("Enter the currency you have chosen: ")   

print(f"{amount} INR is equivalent to {amount*float(currency_dict[currency_chosen])} {currency_chosen}") 

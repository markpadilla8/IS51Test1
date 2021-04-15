


"""
The program is trying to determine which payment option for employees is better (more money).
First option is 100 per day for 10 days. The second option is 1 dollar per day with the amount
being doubled every day for 10 days. There will be two functions used to calculate the pay rate.
Function1 will calculate the amount for the first option, while function2 will calculate the amount for the second option

function1 will output 100 * 10 days.
function2 will loop 10 times, while each time doubling the amount and add the amount to the total. 

if the amount is equal, we output to the user “Option 1 and Option 2 are the same"
if the option1 is better, we output to the user "Option 1 is better"
if the option2 is better, we output to the user "Option 2 is better"
"""

"""
# option 1 
    return 100 * 10

# option 2
    amount = 1
    list1 = []
    loop 10 times
        add amount to list1
        amount *= 2
    sum = sum of all items in loop
    return sum
# main
    var1 = option1
    var2 = option1

    if var1 = var2
        "Option 1 and Option 2 pays the same"
    if var1 < var2
        "Option 2 is better"
    else
        "Option 1 is better"

main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0,10)
        list1.append(amount)
        amount *= 2
    print("list1", list1)
    # total = sum(list1)
    return total


def main():
    pass

var 1 = option1()
option2()
print(var1)

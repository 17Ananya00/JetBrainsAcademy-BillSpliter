print("Enter the number of friends joining (including you):")
num_friends = int(input())
if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    names_dict = dict()
    for i in range(0, num_friends):
        name = input()
        names_dict[name] = 0
    print("Enter the total bill value:")
    bill_value = int(input())
    if bill_value % num_friends == 0:
        each_bill_value = int(bill_value / num_friends)
    else:
        not_rounded = bill_value / num_friends
        each_bill_value = round(not_rounded, 2)

    for name in names_dict:
        names_dict[name] = each_bill_value

    print(names_dict)

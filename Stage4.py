import random

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

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    is_lucky = input()
    if is_lucky == 'Yes':
        lucky = random.choice(list(names_dict))
        print(lucky, "is the lucky one!")

        friends = {f: round(bill_value / (len(names_dict) - 1), 2) for f in names_dict}
        friends[lucky] = 0

        print(friends)
    else:
        print("No one is going to be lucky")
        print(names_dict)




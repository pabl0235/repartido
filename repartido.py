"""
repartido is a small project to split bills
between different people. It is a command line tool 
that allows you to split bills and keep track of who owes what to whom.


Procedure:

1. Create group bill name
To create a group bill name, you can use the command line tool and specify the name of it.
2. Add participants to the group
To add participants to the group, you can use the command line tool and specify the names of the participants.
3. Add expenses to the group
Each participant name will appear in the command line tool and you can specify the expenses for each participant.
4. Calculate who owes what to whom
The command line tool will calculate the total expenses for each participant and determine who owes what to whom
5. Settle up
The command line tool will display the final amounts owed by each participant and allow them to settle up

To code the section "who pays whom", the standard and cleanest approach to practice programming logic is the Greedy Algorithm using two lists (or priority queues / heaps).

Step-by-step logic:

1. Split expenses in two groups: debtors (those with negative balance, but store them as positive numbers to facilitate subtraction) and creditors (those with positive balance). Ignore those with 0 balance.
2. Order both lists from highest to lowest: Sort both lists so that the person who owes the most is matched with the person who is owed the most.
3. Pair and subtract: Take the first debtor and the first creditor. The transfer amount will be the minimum between what the debtor owes and what the creditor is owed.
4. Update and repeat: Subtract that amount from both. The one who reaches 0 exits their list, and the process repeats until both lists are empty.

"""

class participant(object):
    def __init__(self, participant_name):
        self.name = participant_name
        self.expenses = []
        self.balance = 0.0

    def get_total_expenses(self):
        return sum(self.expenses)

print("Enter group bill name:")
group_bill_name = input()

print(f"Group bill name '{group_bill_name}' created successfully!")

print("Enter number of participants:")
num_participants = int(input())

print("Enter participant names:")
participants = []
for i in range(num_participants):
    participant_name = input(f"Participant {i + 1}: ")
    #participants.append(participant_name)
    participants.append(participant(participant_name))

print(f"Participants {participants} added successfully!")

for participant_p in participants:
    print(f"Enter expenses for {participant_p.name}:")
    #expenses = []
    while True:
        expense = input("Enter expense amount (or type 'done' to finish): ")
        if expense.lower() == 'done':
            break
        try:
            participant_p.expenses.append(float(expense))
            #expenses.append(float(expense))
        except ValueError:
            print("Please enter a valid number.")

print("Calculating total expenses for each participant...")

group_total_expenses = 0.0
for participant_p in participants:
    total_expense = participant_p.get_total_expenses()
    print(f"Total expenses for {participant_p.name}: {total_expense}")
    group_total_expenses += total_expense

print(f"Group total expenses: {group_total_expenses}")

deptors = []
creditors = []

for participant_p in participants:
    participant_p.balance = participant_p.get_total_expenses() - (group_total_expenses / num_participants)
    print(f"{participant_p.name} balance: {participant_p.balance}")
    if participant_p.balance < 0:
        deptors.append(participant_p)
    elif participant_p.balance > 0:
        creditors.append(participant_p)

deptors.sort(key=lambda x: abs(x.balance), reverse=True)
creditors.sort(key=lambda x: x.balance, reverse=True)

while deptors and creditors:
    debtor = deptors[0]
    creditor = creditors[0]
    transfer_amount = min(abs(debtor.balance), creditor.balance)
    debtor.balance += transfer_amount
    creditor.balance -= transfer_amount
    print(f"{debtor.name} pays {transfer_amount} to {creditor.name}")
    if debtor.balance == 0.0:
        deptors.pop(0)
    if creditor.balance == 0.0:
        creditors.pop(0)





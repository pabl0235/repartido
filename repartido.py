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

"""
# Source - https://stackoverflow.com/a/3182241
# Posted by yanjost, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-12, License - CC BY-SA 4.0

class participant(object):
    def __init__(self, participant_name):
        self.name = participant_name
        self.expenses = []

    def get_total_expenses(self):
        return sum(self.expenses)
"""
my_objects = []

for i in range(100):
    my_objects.append(participant(f"Participant {i}"))

# Print the name attribute of each instance

for obj in my_objects:
    print(obj.name)
"""

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

for participant_p in participants:
    total_expense = participant_p.get_total_expenses()
    print(f"Total expenses for {participant_p.name}: {total_expense}")

print("Calculating total expenses for each participant...")
    



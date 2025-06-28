# class Party:
#     def __init__(self, people :list):
#         self.people = people
#
#
# people = []
# name = input()
# while name != 'End':
#     people.append(name)
#     name = input()
#
# party = Party(people)
# print(f"Going: " + ", ".join(party.people))
# print(f"Total: " + str(len(party.people)))

class Party:
    def __init__(self):
        self.people = []

party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")


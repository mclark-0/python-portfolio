#maya
guests = [
"Alice", "Bob", "Charlie", "David", "Eve",
"Frank", "Grace", "Heidi", "Ivan", "Judy",
"Kevin", "Liam", "Mallory", "Nia", "Oscar",
"Peggy", "Quinn", "Riley", "Sybil", "Trent",
"Uma", "Victor", "Walter", "Xander", "Yara",
"Zane", "Amari", "Blake", "Casey", "Dakota"
]
#challenge 1.1
plus_one = input("hi bob, what is your friend's name? ")
guests.append(plus_one)
#challenge 1.2
vip_name = input("what is the VIP's name? ")
guests.insert(0, vip_name)
#challenge 1.3
david_index = guests.index("David")
new_friend = input("david can't make it. what is your new friend's name? ")
guests[david_index] = new_friend

print("Updated Guest List")
for guest in guests:
    print(guest)
#challenge 1.4
print("Total Number of Guest Attending: ", len(guests))

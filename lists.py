lucky_numbers = [4, 6, 15, 17, 22]

friends = ["Per", "Pål", "Thomas"]
print(friends[0])

print(friends[1:])

friends[1] = "Geir"
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Lasse")
print(friends)

friends.insert(1, "Stine")
print(friends)

friends.remove("Lasse")
print(friends)

print(friends.index("Stine"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

# Leser inn fra fil inn i en streng -> Splitter streng opp i en liste.print()
# Teller så opp hvert ord fra liste og legger info inn i counts
#   
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1


#print(counts)
# Finner største verdi på både key og verdi

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)



counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts: 
       counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)


# Bruk av get(). Sammenlign med kodesnutt over

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
# Hvis det er et nytt element (navn), da settes teller til 0
    counts[name] = counts.get(name, 0) + 1
print(counts)



File = open('romeo-full.txt', 'r')

# Teller
#count = 0
#for line in File:
#    count = count + 1
#print('Line Count:', count)

# Lese inn data fra fil og skriv ut på skjerm
#raw_data = File.read()
#print('Raw Data:', raw_data)
#raw_data = []
#raw_data.append(File)

# Via funksjon
def read_data(File):
    raw_data = File.read()
    print('Raw Data:', raw_data)
    return raw_data

raw_data = read_data(File)

print(raw_data)


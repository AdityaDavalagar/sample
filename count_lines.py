myfile = "names.txt"
num_names = 0
with open(myfile, 'r') as f:
    for line in f:
        names = line.split()

        num_names += len(names)

print (num_names)
print "hello"

# write to file
with open("f.txt","w") as f:
    f.write("hello world")

# read from file
with open("f.txt","r") as f:
    print f.read()

# this can be used to save python objects
import pickle as pc

# serialize array to file
pc.dump( {1:'2', 2:[3.1415]} , open('f.bin','w'))

# deserialize
print pc.load(open("f.bin"))
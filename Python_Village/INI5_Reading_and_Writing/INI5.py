# Python3 explained / https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files

fout = open('output.txt', 'w')

i = 1

for line in open('rosalind_ini5.txt', 'r'):
    if i%2 == 0:
        fout.write(line)
    i += 1

fout.close()

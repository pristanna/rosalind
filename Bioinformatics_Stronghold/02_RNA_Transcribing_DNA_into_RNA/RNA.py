with open("rosalind_rna.out.txt", "w") as fout:
    with open("rosalind_rna.txt", "r") as fin:
        t = fin.readline()
        u = ""
        for i in t:
            if i == "T":
                u = u + "U"
            else:
                u = u + i
        fout.write(u)

### Other possible solution
# s = raw_input()
# print(t.replace("T", "U"))
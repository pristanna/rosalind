with open("rosalind_revc.out.txt", "w") as fout:
    with open("rosalind_revc.txt", "r") as fin:
        s = fin.readline()
        # [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
        rev = s[::-1]
        rc = ""
        for i in rev:
            if i == "T":
                rc = rc + "A"
            elif i == "A":
                rc = rc + "T"
            elif i == "C":
                rc = rc + "G"
            elif i == "G":
                rc = rc + "C"
            else:
                print(i)
        fout.write(rc)

with open("rosalind_dna.out.txt", "w") as fout:
    with open("rosalind_dna.txt", "r") as fin:
        s = fin.readline()
        a = s.count("A")
        c = s.count("C")
        g = s.count("G")
        t = s.count("T")
        fout.write("{} {} {} {}".format(a, c, g, t))

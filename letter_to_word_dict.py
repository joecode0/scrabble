
def EOWL_to_single_txt(indir, outfilename):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    filelist = []
    huge_list = []
    for i in range(len(alphabet)):
        letter = alphabet[i]
        ffile = indir + letter + " Words.txt"
        filelist.append(ffile)

    for ffile in filelist:
        wordlist = []

        with open(ffile, "r") as f:
            wordlist = f.read().split()

        huge_list.extend(wordlist)

    with open(outfilename, mode="w") as outfile:
        for s in huge_list:
            outfile.write("%s\n" % s)

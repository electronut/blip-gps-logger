gnrmc = open("GNRMC.TXT", "rt")
filtered_gnrmc = open("FILTERED_GNRMC.TXT", "a")

for i,line in enumerate(gnrmc):
    # print "%d : %s" %(i, line)
    # print(i, " : " + line)
    if (line.find(',,,,,,') == -1):
        filtered_gnrmc.write(line)
        print "%d : %s" %(i, line)
        print "------------------------------"

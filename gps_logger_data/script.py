gps_data = open("GPS.TXT", "rt")
gnrmc = open("GNRMC.TXT", "a")

prev_line = ""
next_line = ""

for i,line in enumerate(gps_data):
    # print "%d : %s" %(i, line)
    # print(i, " : " + line)
    if (line.find('GNRMC') != -1):
        prev_line = next_line
        next_line = line
        gnrmc.write(line)
        
        print "%d : %s" %(i, line)
        print "prev_line : %s, next_line : %s" %(prev_line, next_line)
        print "------------------------------"

    # print "prev_line : %s, next_line : %s" %(prev_line, next_line)
    # print "------------------------------"

    # if(i==50):
    #     break


    ,,,,,,

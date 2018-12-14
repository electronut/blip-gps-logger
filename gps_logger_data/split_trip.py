import datetime

filtered_gnrmc = open("FILTERED_GNRMC.TXT", "rt")

prev_line = "$GNRMC,161403.00,A,1305.45179,N,07722.62283,E,36.859,205.47,071218,,,A*4D"
next_line = "$GNRMC,161403.00,A,1305.45179,N,07722.62283,E,36.859,205.47,071218,,,A*4D"

for i,line in enumerate(filtered_gnrmc):
    prev_line = next_line
    next_line = line

    prev_line_splitted = prev_line.split(',')
    next_line_splitted = next_line.split(',')
#     print prev_line_splitted
#     print next_line_splitted

    prev_time = datetime.datetime(2000+int(prev_line_splitted[9][4:6]), int(prev_line_splitted[9][2:4]), int(prev_line_splitted[9][0:2]), int(prev_line_splitted[1][0:2]), int(prev_line_splitted[1][2:4]), int(prev_line_splitted[1][4:6]))
    next_time = datetime.datetime(2000+int(next_line_splitted[9][4:6]), int(next_line_splitted[9][2:4]), int(next_line_splitted[9][0:2]), int(next_line_splitted[1][0:2]), int(next_line_splitted[1][2:4]), int(next_line_splitted[1][4:6]))
    duration = next_time - prev_time
#     print prev_time
#     print next_time
#     print " ----------------- "
#     print prev_time + datetime.timedelta(minutes=30, hours=5)
#     print next_time + datetime.timedelta(minutes=30, hours=5)
#     print duration
#     print "seconds : ", duration.total_seconds()

#     print "----------------------------------------------------"


#     if(i==10):
#         break
    if(duration.total_seconds()>180):
        # print next_line_splitted
        print prev_time
        print next_time
        print "(%d) >> %d : %s" %(duration.total_seconds(), i, line)


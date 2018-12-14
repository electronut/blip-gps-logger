import simplekml, sys

print sys.argv[1]

kml=simplekml.Kml()
gnrmc_data = open(sys.argv[1], "rt")

for i,line in enumerate(gnrmc_data):
    line_splitted = line.split(',')
    nmea_lat = line_splitted[3]
    nmea_lon = line_splitted[5]
    # print "nmea ", nmea_lat, nmea_lon

    lat_dd = int(float(nmea_lat)/100)
    lat_ss = float(nmea_lat) - (lat_dd*100)
    lat = lat_dd + (lat_ss/60)
    # print "lat_ ", lat_dd, lat_ss

    lon_dd = int(float(nmea_lon)/100)
    lon_ss = float(nmea_lon) - (lon_dd*100)
    lon = lon_dd + (lon_ss/60)
    # print "lon_ ", lon_dd, lon_ss

    print lat, lon
    print "------------------------------------------"
    kml.newpoint(coords=[(lon,lat)])

kml.save(sys.argv[1]+'.kml')
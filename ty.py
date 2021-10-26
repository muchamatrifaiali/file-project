#get gps data
from GPSPhoto import gpsphoto
import json
import PIL
import os

#untuk copy file
import shutil
source = ""
destination ="hasil/"

#folder
import os.path
from PIL import Image

#gps distance
from math import sin, cos, sqrt, atan2, radians
# approximate radius of earth in km
R = 6373.0

# convert waktu
import datetime
waktu = 1631626841
detik = 1

counter = 0
detect = 0
distance = 0
restart = 0
nomorCluster=[0]
arrayLat=[-7.637306385102354]
arrayLong=[111.91454313272096]

f = open("folder.txt", "r")
f=f.read()
print(f)
source= f+"/"
# print("mulai")
hapus = open("hasil.csv", "w")
hapus.write("Nama , Longitude , Latitude , golongan \n")
hapus.close()

#f = r'D:\atugas\python\resize photo\foto'
for file in os.listdir(f):
    f_img = f+"/"+file
    print(file)
    lokasi = gpsphoto.getGPSData(f_img)
    tampung = json.dumps(lokasi)
    tampung = json.loads(tampung)
    print(len(tampung))
    if len(tampung)<1:
        continue
    finalLong = json.dumps(tampung["Longitude"])
    finalLat = json.dumps(tampung["Latitude"])
    #print(finalLong)
    #print(",")
    
    
    detect=0
    counter=0
    
    while counter<len(arrayLong):
        lat1 = radians(float(arrayLat[counter])) 
        lon1 = radians(float(arrayLong[counter]))
        lat2 = radians(float(finalLat))
        lon2 = radians(float(finalLong))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c * 1000
        #print(distance)
        if distance < 25:
            detect=1
            restart = counter+1
            counter=2000
        else:
            detect=0
            
        counter=counter+1
        detik = detik+1

    counter = restart
    destination ="hasil/"
    source= f+"/"
    finalName = ""
    if detect==1:
       hasil = str(nomorCluster[counter-1]) +"__"+ file + " , "+ arrayLong[counter-1] + " , " + arrayLat[counter-1]  
       source = source + file
       finalName = destination + str(nomorCluster[counter-1])+ "___" + file
       destination = destination + file
       waktuFinal = nomorCluster[counter-1]
    else:
        arrayLat.append(finalLat)
        arrayLong.append(finalLong)
        nomorCluster.append(len(arrayLong)-1)
        hasil = str(len(arrayLong)-1) +"__" +file + " , "+ finalLong + " , " + finalLat  
        source = source + file
        finalName = destination + str(len(arrayLong)-1)+ "___" + file
        destination = destination + file
        waktuFinal = len(arrayLong)-1
        
     
    shutil.copy(source, destination)
    waktuFinal = waktu+waktuFinal*1000+detik*1
    print(waktuFinal)
    os.utime(destination, (waktuFinal,waktuFinal))
    os.rename(destination, finalName)
    h = open("hasil.csv", "a")
    h.write(hasil)
    h.close()
    print(hasil)
  

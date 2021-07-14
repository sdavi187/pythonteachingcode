# [] create The Weather
# [] copy and paste in edX assignment page
import os
os.system("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt")

temp_file = open("mean_temp.txt","a+")
temp_file.write("Rio de Janeiro,Brazil,30.0,18.0\n")
temp_file.seek(0)
heading = temp_file.readline().strip("\n").split(",")

while True:
    city = temp_file.readline().split(",")

    if city[0] == "":
        break

    print (heading[0].capitalize(), "of", city[0], heading[2], "is", city[2], "Celsius" )

    

temp_file.close()

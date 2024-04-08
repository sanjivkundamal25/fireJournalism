import json

f1 = open("./data/Fire_Incident_Dispatch_Data.csv", "r")
lines = f1.readlines()

dictionary = {}
#create the dictionary here
print(lines)
f1.close()

f2 = open("./data/Fire_Incident_Dispatch_Data.json", "w")
#json.dump(dictionary, f2, indent = 4)

f2.close
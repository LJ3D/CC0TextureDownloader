import requests
import csv

#['assetId', 'downloadAttribute', 'filetype', 'size', 'downloadLink', 'rawLink']
defaultcsv = 'ambientCG_downloads_csv.csv'

with open(defaultcsv, newline='') as f:
	reader = csv.reader(f)
	assets = list(reader)
assets.pop(0)


listOfDownloadAttributes = []
listOfTypes = []
totalSize = 0

for i in assets:
	if i[2] not in listOfTypes:
		listOfTypes.append(i[2])
for i in assets:
	if i[1] not in listOfDownloadAttributes:
		listOfDownloadAttributes.append(i[1])
for i in assets:
	totalSize += int(i[3])


print("Loaded csv file and found:")
print(len(assets), "assets")
print("Assets have the following types:")
print(listOfTypes)
print("Assets have the following download attributes:")
print(listOfDownloadAttributes)
print("All assets combined have a filesize of {0} bytes ({1} gigabytes)".format(totalSize, totalSize/1e+9))

print("Display all asset names? (y/n)")
while True:
	userInput = input()
	if userInput == 'y':
		for i in assets:
			print(i[0] +"__"+ i[1] +"__"+ i[2])
		break
	if userInput == 'n':
		break
	print("Invalid input")

print("Display information of all assets with a certain attribute?: (y/n)")
while True:
	userInput = input()
	if userInput == 'y':
		s = 0
		n = 0
		print("Input download attribute to sort by:")
		attributeInput = input()
		for i in assets:
			if i[1] == attributeInput:
				n += 1
				s += int(i[3])
				print(i[0] +"__"+ i[1] +"__"+ i[2])
		print("{0} assets found with the attribute {1}, with a total size of {2} bytes ({3} gigabytes)".format(n, attributeInput, s, s/1e+9))
		break
	if userInput == 'n':
		break
	print("Invalid input")




print("Display information of all assets with a certain keyword in assetId? (not case sensitive): (y/n)")
while True:
	userInput = input()
	if userInput == 'y':
		s = 0
		n = 0
		print("Enter keyword:")
		keyword = input()
		for i in assets:
			if keyword.upper() in i[0].upper():
				n += 1
				s += int(i[3])
				print(i[0] +"__"+ i[1] +"__"+ i[2])
		print("{0} assets found with the keyword {1}, with a total size of {2} bytes ({3} gigabytes)".format(n, keyword, s, s/1e+9))
		break
	if userInput == 'n':
		break
	print("Invalid input")
	

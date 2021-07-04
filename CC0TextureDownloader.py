import requests
import csv
			if i[2] == "ZIP":
				print("Unzipping {0}_{1}.{2}".format(i[0],i[1],i[2]))
				print(i[0]+'_'+i[1]+'.'+i[2])
				with zipfile.ZipFile(i[0]+'_'+i[1]+'.'+i[2], 'r') as zip_ref:
					zip_ref.extractall(i[0]+'_'+i[1])
		except:
			print("Failed to download {0}_{1} from {2}".format(i[0], i[1], i[4]))
		

#['assetId', 'downloadAttribute', 'filetype', 'size', 'downloadLink', 'rawLink']
defaultcsv = 'ambientCG_downloads_csv.csv'
with open(defaultcsv, newline='') as f:
	reader = csv.reader(f)
	assets = list(reader)
assets.pop(0)
listOfDownloadAttributes = []
totalSize = 0
for i in assets:
	if i[1] not in listOfDownloadAttributes:
		listOfDownloadAttributes.append(i[1])
for i in assets:
	totalSize += int(i[3])


print("Loaded csv file and found {0} assets".format(len(assets)))

print("Would you like to filter assets by a keyword? (not case sensitive) (y/n)")
while True:
	userInput = input()
	if userInput == 'y':
		keyword = input("Enter keyword (NOT CASE SENSITIVE): ")
		break
	if userInput == 'n':
		keyword = None
		break
	print("Invalid input")
print("Would you like to filter assets by a download attribute? (resolution, filetype, etc) (y/n)")
while True:
	userInput = input()
	if userInput == 'y':
		print("Found the following download attributes in the csv file:")
		print(listOfDownloadAttributes)
		print("Substance files have the download attribute '', just press enter if you want to filter for substance files")
		inputValid = False
		while inputValid != True:
			attributeFilter = input("Enter download attribute (CASE SENSITIVE): ")
			if attributeFilter in listOfDownloadAttributes:
				inputValid = True
			else:
				print("Invalid download attribute")
		break
	if userInput == 'n':
		attributeFilter = None
		break
	print("Invalid input")


filteredAssets = getAssetsByFilters(assets, [keyword, attributeFilter])
filteredAssets.sort()
filteredTotalSize = 0
for i in filteredAssets:
	filteredTotalSize += int(i[3])
	
print("found {0} assets that match the filters, with a combined size of {1} bytes ({2} gigabytes)".format(len(filteredAssets), filteredTotalSize, filteredTotalSize/1e+9))

print("Display asset names? (y/n)")
while True:
	userInput = input()
	if userInput == 'y':
		for i in filteredAssets:
			print(i[0]+"_"+i[1])
		break
	if userInput == 'n':
		break
	print("Invalid input")
	
	
print("Would you like to download these assets? (y/n)")
while True:
	userInput = input()
	if userInput == 'y':
		download(filteredAssets)
		break
	if userInput == 'n':
		break
	print("Invalid input")


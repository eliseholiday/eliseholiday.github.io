from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("Bey.gif")
pixelList = list(im.getdata())

#print(pixelList[0])


for i in range(len(pixelList)):
	#print(i)
	redPixel = pixelList[i][0]
	greenPixel = pixelList[i][1]
	bluePixel = pixelList[i][2]
	sum = redPixel + greenPixel + bluePixel
	#print(sum)
	
	if sum < 182:
		#change to darkblue (0 ,51, 76)
		pixelList[i] = darkBlue
	elif sum >= 182 and sum < 364:
		pixelList[i] = red
	elif sum>=364 and sum < 546:
		pixelList[i] = lightBlue
	else:
		pixelList[i] = yellow	

im.putdata(pixelList)
im.show()
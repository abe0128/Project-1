#Abraham De Alba
#CST 205 M,W
#Project 1


from PIL import Image
mylist = []    #my empty list.
im1 = Image.open("Project1Images/1.png")  #my pictures being asked to open.
im2 = Image.open("Project1Images/2.png")
im3 = Image.open("Project1Images/3.png")
im4 = Image.open("Project1Images/4.png")
im5 = Image.open("Project1Images/5.png")
im6 = Image.open("Project1Images/6.png")
im7 = Image.open("Project1Images/7.png")
im8 = Image.open("Project1Images/8.png")
im9 = Image.open("Project1Images/9.png")
mylist.append(im1)    #adding my pictures to my empty list.
mylist.append(im2)
mylist.append(im3)
mylist.append(im4)
mylist.append(im5)
mylist.append(im6)
mylist.append(im7)
mylist.append(im8)
mylist.append(im9)
for pictures in range(0,9):    #setting conditions to determine which
	if(pictures%2 == 1):       #are odd and even.
		print("Odd")
		p = mylist[pictures].convert('L')   #tells computer to turn black and white
		p.show()
	else:
		print("Even")                        #displays even number pictures
		p = mylist[pictures]
		pdata = p.load()
		for i in range(0,p.size[0]-1):           #nested loop
			for j in range(0,p.size[1]-1):
				pix = pdata[i,j]                 
				pix = (pix[1], pix[0], pix[2])   #switching RGB color values to increase green
				pdata[i,j] = pix                 #creating newly made imgage
		p.show()                                 #telling it to show
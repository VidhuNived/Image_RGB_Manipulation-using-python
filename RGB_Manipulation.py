from PIL import Image

# Creating a image object
org_img = Image.open('input.png')

# Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
org_pixelMap = org_img.load()

# Creating new image object with image mode and dimensions as that of original image
new_img = Image.new( org_img.mode, org_img.size)
new_pixelsMap = new_img.load()

# Traversing through the pixel values
for i in range(new_img.size[0]):
    for j in range(new_img.size[1]):
	# Fetching RGB vlaue a pixel to sublist
        list=org_pixelMap[i,j] 
        r=list[0]	# R value
        g=list[1]	# G value
        b=list[2] 	# B value
	# Performing necessary manipulations, the 4th field is for setting aplha value
        new_pixelsMap[i,j] = (r+45,g+45,b+45,255)
org_img.close()
# Display the image
new_img.show()    
# Save the image   
new_img.save("output.png") 
new_img.close()

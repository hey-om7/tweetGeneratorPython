from PIL import Image, ImageDraw, ImageFont

# title max 15char
# desc max row(35 words) & column(9) max
title = "123456789098765"
desc = '''some random text some random textsome
some random text some random textsome
some random text some random textsome
some random text some random textsome
some random text some random textsome
some random text some random textsome
some random text some random textsome'''

fontTitle = ImageFont.truetype('fonts/Roboto-Regular.ttf', 75)
fontDesc = ImageFont.truetype('fonts/Roboto-Light.ttf', 55)
# new = Image.new('RGB', (600, 1200), color=(204, 153, 255))
new = Image.open("bg_2.png")
d = ImageDraw.ImageDraw(new)
d.text((420, 890), title, fill=(255, 255, 255), font=fontTitle)
d.text((220, 1090), desc, fill=(255, 255, 255), font=fontDesc)
new.show()


# from PIL import ImageFont, ImageDraw, Image

# image = Image.open('hsvwheel.png')
# draw = ImageDraw.Draw(image)
# txt = "Hello World"
# fontsize = 1  # starting font size

# # portion of image width you want text width to be
# img_fraction = 0.50

# font = ImageFont.truetype("arial.ttf", fontsize)
# while font.getsize(txt)[0] < img_fraction*image.size[0]:
#     # iterate until the text size is just larger than the criteria
#     fontsize += 1
#     font = ImageFont.truetype("arial.ttf", fontsize)

# # optionally de-increment to be sure it is less than criteria
# fontsize -= 1
# font = ImageFont.truetype("arial.ttf", fontsize)

# print('final font size', fontsize)
# draw.text((10, 25), txt, font=font)  # put the text on the image
# image.save('hsvwheel_txt.png')

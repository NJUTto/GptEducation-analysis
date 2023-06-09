from PIL import Image, ImageDraw, ImageFont

# Open the first image and add whitespace to the top
img1 = Image.open("./Newbing.png")
width, height = img1.size
new_height = height + 150
new_img1 = Image.new("RGB", (width, new_height), (255, 255, 255))
new_img1.paste(img1, (0, 150))

new_img1.save("./whitespace/Newbing.png")

# # Add title to the first image
# draw = ImageDraw.Draw(new_img1)
# font = ImageFont.truetype("arial.ttf", 50)
# title = "Image 1 Title"
# title_width, title_height = draw.textsize(title, font)
# draw.text(((width - title_width) / 2, 20), title, font=font, fill=(0, 0, 0))

# Open the second image and add whitespace to the top
# img2 = Image.open("./topic_pic/AI-4.png")
# width, height = img2.size
# new_height = height + 100
# new_img2 = Image.new("RGB", (width, new_height), (255, 255, 255))
# new_img2.paste(img2, (0, 100))

# # Add title to the second image
# draw = ImageDraw.Draw(new_img2)
# font = ImageFont.truetype("arial.ttf", 50)
# title = "Image 2 Title"
# title_width, title_height = draw.textsize(title, font)
# draw.text(((width - title_width) / 2, 20), title, font=font, fill=(0, 0, 0))

# # Combine the two images horizontally
# combined_img = Image.new("RGB", (width * 2, new_height), (255, 255, 255))
# combined_img.paste(new_img1, (0, 0))
# combined_img.paste(new_img2, (width, 0))

# Save the combined image

# new_img2.save("./topic_pic_combine/AI.png")
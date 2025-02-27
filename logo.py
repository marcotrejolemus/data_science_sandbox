from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

width = 500
height = 500
canvas = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(canvas)

# Guitar Pick shape
draw.ellipse([(100, 100), (400, 400)], fill='black')

# Lightning bolt
draw.polygon([(250, 200), (300, 300), (250, 350), (350, 250), (200, 250)], fill='red')

# Text
font = ImageFont.truetype('D:/rockband.jpg', 40)  # Replace with the path to a desired font file
text = "Your TikTok Channel Name"
text_width, text_height = draw.textsize(text, font=font)
text_position = ((width - text_width) // 2, 420)
draw.text(text_position, text, font=font, fill='black')

plt.imshow(canvas)
plt.axis('off')
plt.show()

canvas.save('D:/logo.png')
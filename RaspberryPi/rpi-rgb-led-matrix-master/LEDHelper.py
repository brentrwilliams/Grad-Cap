from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def getTextImage(text, backgroundColor=(0,0,0), textColor=(255,255,255)):
   font = ImageFont.truetype("DroidSans.ttf", 28)
   (width,height) = font.getsize(text)
   image = Image.new("RGB", (width+2, 32), backgroundColor) # Can be larger than matrix if wanted!!
   draw  = ImageDraw.Draw(image)
   draw.text((1, 1), text, font=font, fill=textColor)
   return image
   

def main():
   image = getTextImage("Hi Mom!")
   image.show()


if __name__ == '__main__':
   main()
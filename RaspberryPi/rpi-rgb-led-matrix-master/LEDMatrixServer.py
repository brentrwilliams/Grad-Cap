#!/usr/bin/python

import Image
import ImageDraw
from LEDHelper import getTextImage
from rgbmatrix import Adafruit_RGBmatrix
from time import sleep
import serial

# Path for raspberry pi
arduionoPath = '/dev/ttyACM0'

# Path for Mac
# arduionoPath = '/dev/cu.usbmodem1451'

def clear(arduino, matrix, line):
   print("* Clearing the screen")
   matrix.Clear()
   return arduino.readline()


def drawImage(arduino, matrix, line):
   imageName = line.split(' ', 1)[1].rstrip()
   print('* Drawing image "' + imageName + '" to screen')
   matrix.Clear()
   return arduino.readline()


def writeText(arduino, matrix, line):
   text = line.rstrip()
   print('* Writing text "' + text + '"')
   image = getTextImage(text)
   
   while arduino.inWaiting() <= 0:
      for n in range(32, -image.size[0], -1):
         matrix.SetImage(image.im.id, n, 1)
         sleep(0.025)

         # If there is another command waiting
         if arduino.inWaiting() > 0:
            matrix.Clear()
            return arduino.readline()
   
   matrix.Clear()
   return arduino.readline()


def main():
   commands = {
      '#clear': clear,
      '#image': drawImage
   }
   # Rows and chain length are both required parameters:
   matrix = Adafruit_RGBmatrix(32, 1)
   arduino = serial.Serial(arduionoPath, 9600) # Establish the connection on a specific port
   line = arduino.readline() # Read the newest output from the Arduino 

   while True:
      if line == None:
         line = arduino.readline()
         # continue
      print(line)
      firstWord = line.split(' ', 1)[0].rstrip()

      if firstWord in commands:
         line = commands[firstWord](arduino, matrix, line)
      else:
         line = writeText(arduino, matrix, line)



if __name__ == '__main__':
   main()


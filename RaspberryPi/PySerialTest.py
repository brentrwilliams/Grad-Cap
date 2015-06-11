from time import sleep
import serial

# Path for raspberry pi
# arduionoPath = '/dev/ttyACM0'

# Path for Mac
arduionoPath = '/dev/cu.usbmodem1451'

def clear(line):
   print("* Clearing the screen")


def drawImage(line):
   imageName = line.split(' ', 1)[1].rstrip()
   print('* Drawing image "' + imageName + '" to screen')

def writeText(line):
   print('* Writing text "' + line.rstrip() + '"')


def main():
   commands = {
      '#clear': clear,
      '#image': drawImage
   }
   ser = serial.Serial(arduionoPath, 9600) # Establish the connection on a specific port
   
   while True:
      line = ser.readline() # Read the newest output from the Arduino 
      print(line)

      firstWord = line.split(' ', 1)[0].rstrip()
      if firstWord in commands:
         commands[firstWord](line)
      else:
         writeText(line)

      sleep(.1) # Delay for one tenth of a second



if __name__ == '__main__':
   main()
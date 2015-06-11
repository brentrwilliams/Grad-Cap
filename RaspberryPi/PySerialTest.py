from time import sleep
import serial

def main():
   # Path for raspberry pi
   arduionoPath = '/dev/ttyACM0'

   # Path for Mac
   # arduionoPath = '/dev/cu.usbmodem1451'

   ser = serial.Serial(arduionoPath, 9600) # Establish the connection on a specific port
   
   while True:
        print ser.readline() # Read the newest output from the Arduino
        sleep(.1) # Delay for one tenth of a second



if __name__ == '__main__':
   main()
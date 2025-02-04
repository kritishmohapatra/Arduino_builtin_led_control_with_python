#THIS CODE IS A BASIC PYTHON CODE WHICH CAN CONTROL THE IN-BUILT LED OF ARDUINO BOARD
#COPYRIGHT - Kritish Mohapatra





#import the pyfirmata2 module install it by pip by this command - pip install pyfirmata2
import pyfirmata2

#write your port number 
port="COM4"

#initialize the board as Arduino with port
board=pyfirmata2.Arduino(port)

'''board.get_pin(): This is a method call. It's accessing the get_pin() method of the board object. This method is used to obtain a reference to a specific pin on the Arduino board'''

''''d:13:o': This is a string argument passed to the get_pin() method. It specifies the pin configuration:
    1. d: Indicates that we're dealing with a digital pin.
    2. 13: Specifies the number of the pin on the Arduino board.
    3. o: Sets the pin mode to output.'''

led=board.get_pin('d:13:o')
while True:
    k=int(input("Enter the value here:-"))
    led.write(k)
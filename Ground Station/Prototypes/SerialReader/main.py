import serial
import time
import matplotlib.pyplot as plt

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9800, timeout=1)
time.sleep(2)

data = []
for i in range(50):
    line = ser.readline()   # read a byte string
    if line:
        string = line.decode().strip()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        print(num)
        data.append(num) # add int to data list
ser.close()

# build the plot
plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Button State')
plt.title('Button State vs. Time')
plt.show()
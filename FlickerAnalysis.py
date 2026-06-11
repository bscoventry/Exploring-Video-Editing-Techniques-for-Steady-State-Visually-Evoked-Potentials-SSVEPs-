import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft,fftfreq
import pdb
fs = 2023 #10k for other videos, 2.023k for ScreenA1. Don't use A1_Screen and similar files, unknown sample rate
import struct

def read_16bit_signed_binary(file_path):
    """
    Reads a binary file containing 16-bit signed integers.

    Args:
        file_path (str): The path to the binary file.

    Returns:
        list: A list of 16-bit signed integers read from the file.
    """
    data = []
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(2)  # Read 2 bytes (16 bits) at a time
            if not chunk:
                break  # End of file
            value = struct.unpack('<h', chunk)[0]  # Unpack as little-endian signed short
            data.append(value)
    return data

# Example usage:
#4,8
file_path = 'ScreenB4.bin'  # Replace with your file path
data = read_16bit_signed_binary(file_path)

#print(data)
#df = pd.read_csv('SSVEP.csv')
#plt.plot(df['Time (s)'],df['Channel 1 (V)'])
#plt.show()
plt.plot(data)
plt.show()
srange1 = (2400,21800)#ScreenB3(2300,22200)#ScreenB2(1900,21800)#ScreenB1(1890,21900)#ScreenA4(2000,21100)#ScreenA3(2000,21550)#ScreenA2(3600,23400)#(3900,23400)ScreenA1#A1Screen#(859000,958000)#WSR2,4#(1708500,1808000)#WSR2,8#(44700,138200)#C1_Retry#(36260,128500)#H4_Retry#(27000,124750)#F1_retry#(52000,153000)#F1#(37000,135700)#E2#(47000,147000)#D1#(45000,144000)#C1#(28000,128000)#A2#(147000,346800)#A1#(44000,144000)#H4#(34000,135000)#H2#(45280,146000)#H1
#srange1 = (1650000,1760000)#(30770,35822) #Video 1: (134000,233800) Video 2:(344756,444022) Video 3: (563682,663680) Video 4: (780000,900000) Video 5: (1000000,1120000) Video 6: (1225010,1324300) Video 7: (1425000,1540000) Video 8: (1650000,1760000)
Flicker = data#df['Channel 1 (V)'].values
Flick1 = Flicker[srange1[0]:srange1[1]]
plt.plot(Flick1)
plt.show()
N = len(Flick1)
T = 1./fs
YF = fft(Flick1)
XF = fftfreq(N, T)[:N//2]
plt.plot(XF, 2.0/N * np.abs(YF[0:N//2]))
plt.show()
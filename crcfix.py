import struct
import argparse
import binascii
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-file", '-f', type=str, default=None, required=True,
                    help="File Name")
parser.add_argument("-count", '-c', type=int, default=4096, required=False,
                    help="Number of times to count")
args = parser.parse_args()

file = args.file
count = args.count

fr = open(file, 'rb').read()
data = bytearray(fr[0x0c:0x1d])
crc32key = eval('0x'+str(binascii.b2a_hex(fr[0x1d:0x21]))[2:-1])

print('\nPlease wait...')
n = count
for w in range(n):
    width = bytearray(struct.pack('>i', w))
    for h in range(n):
        height = bytearray(struct.pack('>i', h))
        for x in range(4):
            data[x+4] = width[x]
            data[x+8] = height[x]
        crc32result = binascii.crc32(data) & 0xffffffff
        if crc32result == crc32key:
            print('\nWidth: ' + str(width))
            print('Height: ' + str(height))
            newpic = bytearray(fr)
            for x in range(4):
                newpic[x+16] = width[x]
                newpic[x+20] = height[x]
            fw = open(file + '_crcfix.png', 'wb')
            fw.write(newpic)
            print('\nOK: ' + str(file + '_crcfix.png'))
            fw.close
            sys.exit()

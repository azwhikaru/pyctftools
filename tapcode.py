import argparse

mapList = []
mapRow1 = ['A', 'B', 'C', 'D', 'E']
mapRow2 = ['F', 'G', 'H', 'I', 'J']
mapRow3 = ['L', 'M', 'N', 'O', 'P']
mapRow4 = ['Q', 'R', 'S', 'T', 'U']
mapRow5 = ['V', 'W', 'X', 'Y', 'Z']
mapList.append(mapRow1)
mapList.append(mapRow2)
mapList.append(mapRow3)
mapList.append(mapRow4)
mapList.append(mapRow5)

mapListEX = []
mapRow1EX = ['. ./', '. ../', '. .../', '. ..../', '. ...../',]
mapRow2EX = ['.. ./', '.. ../', '.. .../', '.. ..../', '.. ...../']
mapRow3EX = ['... ./', '... ../', '... .../', '... ..../', '... ...../']
mapRow4EX = ['.... ./', '.... ../', '.... .../', '.... ..../', '.... ...../']
mapRow5EX = ['..... ./', '..... ../', '..... .../', '..... ..../', '..... ...../']
mapListEX.append(mapRow1EX)
mapListEX.append(mapRow2EX)
mapListEX.append(mapRow3EX)
mapListEX.append(mapRow4EX)
mapListEX.append(mapRow5EX)

def encode(text):
    textInput = str(text).upper()
    textList = []

    tapCode = ''

    for count in range(len(textInput)):
        textList.append(textInput[count])

    for a in range(len(textList)):
        for x in range(len(mapList)):
            for y in range(len(mapList[x])):
                if mapList[x][y] == textList[a]:
                    tapCode = tapCode + mapListEX[x][y] + ' '
    tapCode = tapCode.strip()
    
    return(tapCode)

def decode(code):
    codeInput = code
    codeInput = codeInput.strip('/')
    codeList = codeInput.split('/')

    plainText = ''

    for count in range(len(codeList)):
        countCode = codeList[count].strip()
        countCodeList = countCode.split(' ')

        countNum = int(countCodeList[0].count(".")) - 1
        countNumB = int(countCodeList[1].count(".")) - 1

        plainText = plainText + mapList[countNum][countNumB] + ', '

    return(plainText.strip(', '))

parser = argparse.ArgumentParser()
parser.add_argument("-action", '-a', type=str, default=None, required=True,
                    help="d -> Decode Tap Code\ne -> Encode Tap Code")
parser.add_argument("-text", '-t', type=str, default=None, required=True,
                    help="Text U need to en/decode")
args = parser.parse_args()

action = args.action
text = args.text

if(action == 'd'):
    print('OK [' + decode(text) + ']')
    exit(0)
if(action == 'e'):
    print('OK [' + encode(text) + ']')
    exit(0)
else:
    print('An undefined operation was entered.')
    exit(1)

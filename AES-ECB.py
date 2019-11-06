from Cryptodome.Cipher import AES
import binascii


def getDetermenisticKeys():
    l = []
    keys = open("C:/Users/a.gegaj/Documents/FIEK-Master/Siguri e informacionit/keys.txt", "r")
    for key in keys:
        k3 = key[6] + key[7]
        k0 = key[0] + key[1]
        k5 = key[10] + key[11]
        k4 = key[8] + key[9]
        if(int(k3, 16) < int("2b", 16) and int(k0, 16) < int(k5, 16) and int(k4, 16) < int("20", 16)):
            l.append(key)
            
    return l


def getCandidateKeys():
    l = getDetermenisticKeys()
    candidateKeys = []
    hexlist = [bytes(range(16))[x:x+1].hex()[1] for x in bytes(range(16))]
    for k in l:
        c = []
        for hex in hexlist:
            for h in hexlist:
                for a in hexlist:
                    for b in hexlist:
                        c = k.rstrip() + hex + h + a + b
                        candidateKeys.append(c)

    return candidateKeys 

 
def decrypt(cipher, key): 
    decipher = AES.new(bytearray.fromhex(key), AES.MODE_ECB)
    plainText = decipher.decrypt(bytearray.fromhex(cipher))
   
    return plainText


def findCode(cipher):
    keys = getCandidateKeys()
    for key in keys:
        plainText = decrypt(cipher, key)
        if chr(plainText[0]) == 'G' and chr(plainText[1]) == 'R' and chr(plainText[3]) == '0' and chr(plainText[4]) == '4':
            print("Key: " + key)
            print("Mesazhi i dekriptuar: " + str(plainText, 'utf-8'))
            print("KODI : "+ str(plainText, 'utf-8')[11:])
            break


findCode('6ba84490e67cfba8fd07354d2899b58f') 
    
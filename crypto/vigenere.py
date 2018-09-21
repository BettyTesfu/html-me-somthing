from helpers import alphabet_position, rotate_character

def keyPosition(key):
    otext = [alphabet_position(i) for i in key]
    return otext
def encrypt (text,key):
    newText = ""
    key_length = len(key)
    counter = 0
    new_key = keyPosition(key) 
    for i in text:
        if i.isalpha():
            newText = newText + rotate_character(i ,new_key[counter % key_length])
            counter = counter+1
        else:
            newText = newText + i
    return newText

def main():
     x = input("Type a message: ")
     y = input("Rotate by: ")
     result = encrypt(x, y)
     print (result)

if __name__ == '__main__':
    main()
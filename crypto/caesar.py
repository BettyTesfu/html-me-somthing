from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    list1 = ""
    for char in text:
        list1 += rotate_character(char, rot)
    return list1
def main():
    x = input("Type a message: ")
    y = int(input("Rotate by: "))
    result = encrypt(x, y)
    print (result)
if __name__ == '__main__':
    main()
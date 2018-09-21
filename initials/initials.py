def get_initials(fullname):
    answere =[]
    name_list =fullname.split(" ")
    for word in name_list:
        answere.append(word[0].upper())
    return ' '.join(answere)
def main():
      inp = input("Type your name")
      print(get_initials(inp))
if __name__ == '__main__':
    main()
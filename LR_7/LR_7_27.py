import textwrap


def main():
    with open("res/LR_7/27_text.txt") as file:
        text_content = file.read()

    print("Initital text:")
    print(textwrap.fill(text_content, 80, initial_indent="    "))
    
    print()
    while True:
        char = input("Enter char: ")
        if len(char) != 1:
            print("Not a char")
            continue
        
        string = input("Enter the string: ")
        if len(string) == 0:
            print("String is empty")
            continue
        
        break
    print()
    
    text_result = ""
    
    # simple solution
    # text_result = text_content.replace(char, string)
    
    for ch in text_content:
        text_result += string if ch == char else ch
    
    print("Resulted text:")
    print(textwrap.fill(text_result, 80, initial_indent="    "))
    
    
    
if __name__ == "__main__":
    main()

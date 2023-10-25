def main():
    with open("res/LR_8/4_f.txt") as f, \
         open("res/LR_8/4_tmp.txt", "w+") as tmp, \
         open("res/LR_8/4_g.txt", "w+") as g:
             
        print("F-file:")
        for c, line in enumerate(f, 1):
            print("[{c}]: {line}".format(c=c, line=line.replace("\n", "")))
            if int(line) < 0:
                print(" └─ to TMP")
                tmp.write(line)
            else:
                print(" └─ to G-file")
                g.write(line)
        print()     
            
        tmp.seek(0) 
            
        print("TMP:")
        for c, line in enumerate(tmp, 1):
            print("[{c}]: {line}".format(c=c, line=line.replace("\n", "")))
            g.write(line)
        print(" └─ Append to G-file")      
        print()  
            
        g.seek(0)
            
        print("G-file:")
        for c, line in enumerate(g, 1):
            print("[{c}]: {line}".format(c=c, line=line.replace("\n", "")))
                


if __name__ == "__main__":
    main()

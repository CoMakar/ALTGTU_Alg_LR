from importlib import import_module
import traceback as tb
from pathlib import Path


print("[- Press Ctrl-C to exit -]")

lr_files = [f.name.rstrip(".py") for f in Path.cwd().rglob("LR_*_*.py")]

print("Files:")
for file in lr_files:
    print(" - {}".format(file))
print()


try:
    while True:
        print("[?] Run LR_N_V:")
        lr_n = input("    N: ")
        var = input("    V: ")
        
        lr_name = "LR_{lr}_{var}".format(lr=lr_n, var=var)
        lr_path = "LR_{lr}.{lr_name}".format(lr=lr_n, lr_name=lr_name)

        try:
            if lr_name not in lr_files:
                print("[-] Not found: LR_{lr}.LR_{lr}_{var}".format(lr=lr_n, var=var))
                continue
            
            lr_module = import_module(lr_path)
            
            print()
            print(" ~  {}".format(lr_name))
            print("-"*80)
            
            lr_module.main()
            
            print("-"*80)
            print("[+] LR finished")
            print()
            
        except Exception as e:
            print("[!] Error:")
            print("~"*80)
            tb.print_exc()
            print("~"*80)

except KeyboardInterrupt:
    print()
    print("[- End -]")

import traceback as tb
import itertools as ittls
from importlib import import_module
from pathlib import Path


restricted_dirs = {"lib", "res", ".vscode", ".git"}
cwd = Path.cwd()
dirs = [
    f for f in cwd.iterdir() if f.is_dir() and f.name not in restricted_dirs
]
dir_files = {
    d.name:
    [
        "{d}.{f}".format(d=d.name, f=f.name.rstrip(".py"))
        for f in d.glob("*.py")
        if f.name != "__init__.py"
    ]
    for d in dirs
}
files = list(ittls.chain.from_iterable(dir_files.values()))


print("[- Press Ctrl-C to exit -]")
print("Files:")
for dir in dir_files:
    print("  {}".format(dir))
    for file in dir_files[dir]:
        print("   └─ {}".format(file))
print()


try:
    while True:
        print("[?] Run:")
        to_run = input(">>> ")
        
        if to_run not in files:
            print(
                "[-] Not found: {tr}".format(
                    tr=to_run
                )
            )
            continue

        try:
            run_module = import_module(to_run)

            print()
            print(" ~  {}".format(to_run))
            print("-" * 80)

            run_module.main()

            print("-" * 80)
            print("[+] finished")
            print()

        except Exception as e:
            print("[!] Error:")
            print("~" * 80)
            tb.print_exc()
            print("~" * 80)

except KeyboardInterrupt:
    print()
    print("[- End -]")

import sys, os, errno
from rich import print
from rich.progress import track
from random import randrange, choice

if len(sys.argv) != 2:
    print("Generator plikow z danymi dla projektu [i]Lizak[/i]")
    print("Uzycie: py generator.py [i]<ilosc plikow>[/i]")
    print("\nGenerator tworzy pliki o nazwie [i]<indeks>.txt[/i], indeks -> 1, 2, ..., <ilosc plikow>")
    sys.exit(1)

num_files = int(sys.argv[1])

try:
    os.mkdir("in")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for i in track(range(num_files), description="Generowanie..."):
    with open(f"in/{i+1}.txt", "w+") as f:
        n = randrange(1, 1_000_00)
        m = randrange(1, 1_000_00)
        f.write(f"{n} {m}\n")

        choices = ["T", 'W']
        lollipop = ""
        for j in range(n):
            lollipop += choice(choices)
        f.write(lollipop + "\n")

        price_list = ""
        for i in range(m):
            price_list += str(randrange(1, 2_000_00)) + "\n"

        f.write(price_list)

print(f"Wygenerowano {num_files} plikow!")

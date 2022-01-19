import errno
import os
from glob import glob

from rich.progress import track


def solve_lollipop(lollipop, value, n):
    new_lollipop = None
    prev_sum = 0
    i = 0
    while i < n:
        if new_lollipop:
            break

        j = i
        total_sum = prev_sum
        while j < n:
            total_sum += lollipop[j]
            if total_sum == value:
                new_lollipop = (i, j)
                break
            elif total_sum > value:
                total_sum = 0
                break
            j += 1

        prev_sum = total_sum
        i += j + 1

    return new_lollipop


def save_to_out(data, filename):
    try:
        os.mkdir("out")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    open(f".\\out\\{filename}", 'w+').write(data)


def main():
    in_files = glob('.\\in\\*.txt')
    for in_file in in_files:
        with open(in_file) as file:
            lines = file.readlines()
            (num_segments, num_k) = [int(i) for i in lines[0].split()]
            lollipop = lines[1].strip()

            if num_segments != len(lollipop):
                print("Podany lizak jest nieprawidlowy:")
                print(f"\tZadano {num_segments}-segmentowy lizak, a podano tylko {len(lollipop)} segmentów")
                return

            k_values = []
            for line in lines[2:]:
                k_values.append(int(line))

            price_table = {'T': 2, 'W': 1}
            price_only_lollipop = [price_table[i] for i in lollipop]

            out_data = ""
            for k in track(range(len(k_values)), description=f"Przetwarzanie pliku {in_file}..."):
                new_lollipop = solve_lollipop(price_only_lollipop, k_values[k], num_segments)
                if new_lollipop:
                    out_data += f"{new_lollipop[0] + 1} {new_lollipop[1] + 1}\n"
                else:
                    out_data += "NIE\n"

            out_filename = in_file.split('\\')[-1]
            save_to_out(out_data, out_filename)


if __name__ == '__main__':
    main()

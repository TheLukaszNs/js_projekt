from glob import glob
from shutil import copy2
from datetime import datetime


def add_in_fragment(n, m):
    temp_to_add = ""
    temp_to_add += f"<div class='in-item'>" \
                   f"<span>Liczba segmentów: <b>{n}</b></span>" \
                   f"<span>Ilość rozpatrywanych warości: <b>{m}</b></span>" \
                   f"</div>"
    return temp_to_add


def add_out_fragment():
    pass


def add_lollipop(lizak):
    temp_to_add = ""
    temp_to_add += f"<div class='lolipop'>"
    for i in range(len(lizak)):
        temp_to_add += f"<div class='lolipop-item-char char-{lizak[i]}'></div>"
    temp_to_add += f"</div>"
    return temp_to_add


def main():
    template = '' \
               '<html>' \
               '<head>' \
               '<title>Zadanie Lizak - Łukasz Myśliwiec</title>' \
               '<link rel="stylesheet" href="./styles.css" />' \
               '</head>' \
               '<body>'
    files_in = glob('.\\in\\*.txt')
    files_out = glob('.\\out\\*.txt')
    template += '<div class="page-header">' \
                '<a class="header-name" href="https://github.com/TheLukaszNs" target="_blank">Łukasz Myśliwiec</a>' \
                '<div>Języki Skryptowe - Zadanie Lizak</div>' \
                '</div>'
    for (i, file_path) in enumerate(files_in):
        file_name = file_path.split('\\')[-1]
        template += '<div class="data-item">'
        n, m = None, None
        lizak = None
        count_created = 0
        with open(file_path, 'r') as f:
            (n, m) = f.readline().split()
            lizak = f.readline().strip()

        with open(files_out[i], 'r') as f:
            lines = [line.strip() for line in f]
            for line in lines:
                if line != 'NIE':
                    count_created += 1

        template += add_in_fragment(n, m)
        template += "<div class='hidden'>"
        template += add_lollipop(lizak)
        template += f"<br /><br />" \
                    f"<span>Liczba utworzonych lizaków: <b>{count_created}</b></span>"
        template += "</div>"
        template += '</div>'

    template += '<script src="./script.js"></script>' \
                '</body>' \
                '</html>'

    with open('RAPORT.html', 'w+') as f:
        f.write(template)

    copy2('RAPORT.html', f"./raporty/RAPORT {datetime.now().strftime('%Y-%m-%d-%I.%M.%S')}.html")

    print('Gotowe!')


if __name__ == '__main__':
    main()

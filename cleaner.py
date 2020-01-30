import re
from sys import exit

try:
    import pysrt
except:
    print('Missing dependency: pip3 install --user pysrt')
    exit(2)

ADS = ['[###]',
       '.*a Card Shark AMERICASCARDROOM.*',
       '.*Advertise your product or brand here.*',
       '.*Apóyanos y conviértete en miembro VIP Para.*',
       '.*Addic7ed.*',
       '.*argenteam.*',
       '.*AllSubs.*',
       'Created and Encoded by.*',
       '.*corrected.*by.*',
       '.*Entre a AmericasCardroom. com Hoy.*',
       '.*Everyone is intimidated by a shark. Become.*',
       '.*Juegue Poker en Línea por Dinero Real.*',
       '.*OpenSubtitles.*',
       '.*Resync.*for.*',
       '.*Resync.*improved.*',
       '.*Ripped?By.*',
       '.*Sigue "Community" en.*',
       '.*Subtitles.*by.*',
       '.*Subt?tulos.*por.*',
       '.*Support us and become VIP member.*',
       '.*Subs.*Team.*',
       '.*subscene.*',
       '.*Subtitulado por.*',
       '.*subtitulamos.*',
       '.*Synchronized.*by.*',
       '.*Sincronizado y corregido por.*',
       '.*subdivx.*',
       '.*Sync.*Corrected.*',
       '.*Sync.*corrections.*by.*',
       '.*sync and corrections by.*'
       '.*Sync.*by.*',
       '.*Una.*traducci?n.*de.*',
       '.*tvsubtitles.*',
       '.*Una.*traducci?n.*de.*',
       'Tacho8',
       '.*www. com.*',
       '.*www. es.*'
]

def ads_in_line(line):
    for pt in ADS:
        if re.match(pt, line):
            return True
    return False

if __name__ == '__main__':
    from sys import argv
    from shutil import move

    if '-h' in argv:
        print('Usage: python3 cleaner.py <sub1> <sub2> <sub3> <...>')
        exit()

    for filename in argv[1:]:
        subs = pysrt.open(filename)
        for i, line in enumerate(subs):
            modified = False
            if ads_in_line(line.text):
                print("Removing:", line)
                print()
                del subs[i]
                modified = True
        if modified:
            move(filename, filename+'.bak')
            subs.save(filename)

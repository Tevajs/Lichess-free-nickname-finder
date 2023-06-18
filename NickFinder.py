import time

import requests
import ndjson
from itertools import product
from threading import Thread
import pandas as pd

username = "BigFaatAss"
alff = "abcdefghijklmnopqrstuvwxyz"

FileName = "NotCorrectNicks.txt"
FileOfCorr = "CorrectNicks.txt"

def responseGet(url, headers, proxies):
    try:
        n = requests.get(url, headers=headers,
                         proxies=proxies)
        return n
    except Exception as e:
        time.sleep(0.2)
    return 0


def obrab(i, notcorrect,  alf):
    name = i

    f = open(FileName, "a")

    if i + "\n" not in notcorrect and not i.startswith('_') and not i.startswith('-') and not i.endswith(
            '_') and not i.endswith('-'):
        # print("sss")
        time.sleep(0.1)
        try:
            # print("sss")
            rr = requests.get(f"https://lichess.org/api/player/autocomplete?term={i}&exists=1")
            #print(rr.status_code)
            if rr.text == "false":
                filer = open(FileOfCorr, "r")
                a = filer.readlines()
                filer.close()
                filer = open(FileOfCorr, "a")

                if i+"\n" not in a :
                    filer.write(''.join(i)+"\n")
                filer.close()
                print(''.join(i))

            elif rr.status_code == 429:
                time.sleep(3)
                obrab(i, notcorrect, alf)
            else:
                f.write(i + "\n")


        except Exception as e:
            print(e)
            time.sleep(2)
            obrab(i, notcorrect, alf)
    f.close()


        # print(response.status_code)


def allNicksWithRange(rangee: int, includeNums: bool, includeCherts: bool,):
    f = open(FileName, "r")
    # print(notcorrect)
    notcorrect = f.readlines()
    f.close()
    alf = alff
    if includeNums:
        alf += "1234567890"
    if includeCherts:
        alf += "-_"
    for i in product(alf, repeat=rangee):
        c = 0
        if "".join(i) + "\n" in notcorrect:
            continue
        else:
            time.sleep(1)
            thread = Thread(target=obrab, args=("".join(i), notcorrect, alf,))

        # response = requests.get(f"https://lichess.org/api/user/{''.join(i)}")
        thread.start()


def allNicksStartWithAndRange(starts: str, rangee: int, includeNums: bool, includeCherts: bool,):
    f = open(FileName, "r")
    # print(notcorrect)
    notcorrect = f.readlines()
    f.close()
    alf =alff
    if includeNums:
        alf += "1234567890"
    if includeCherts:
        alf += "-_"
    for i in product(alf, repeat=rangee):
        c = 0
        if starts.join(i)  + "\n" in notcorrect:
            continue
        else:
            time.sleep(1.5)
            thread = Thread(target=obrab, args=(starts.join(i), notcorrect, alf))

        # response = requests.get(f"https://lichess.org/api/user/{''.join(i)}")
        thread.start()


##print(response)
filer = open(FileOfCorr, "a")
filer.close()

allNicksWithRange(3, True, True)
import keyboard as key
import time


def youtube():
    key.press('win')
    key.press('r')
    key.release('win')
    key.release('r')
    time.sleep(1)
    key.write("https://youtube.com")
    key.send("enter")
def twitch():
    key.press('win')
    key.press('r')
    key.release('win')
    key.release('r')
    time.sleep(1)
    key.write("https://twitch.tv")
    key.send("enter")
def zak():
    key.press('win')
    key.press('r')
    key.release('win')
    key.release('r')
    time.sleep(1)
    key.write("https://twitch.tv/ZakvielChannel")
    key.send("enter")
def ds():
    key.press('win')
    key.press('r')
    key.release('win')
    key.release('r')
    time.sleep(1)
    key.write("https://discord.com/app")
    key.send("enter")
def mine():
    key.press('win')
    key.press('r')
    key.release('win')
    key.release('r')
    time.sleep(1)
    key.write("C:\\Users\\Admin\\Desktop\\Minecraft\\TLauncher.lnk")
    key.send('enter')
def gmail():
    key.press('win')
    key.press('r')
    key.release('win')
    key.release('r')
    time.sleep(1)
    key.write("https://gmail.com")
    key.send("enter")
def shutdown():
    key.press('win')
    key.press('r')
    key.release('win')
    key.release('r')
    time.sleep(1)
    key.write("shutdown -s -t 00")
    key.send("enter")
def main():
    print("available commands:\nzak - twitch ZakviakvielChannel\nyt - youtube.com\ntwitch - twitch.tv\nmine - minecraft\nds - discord\ngmail - gmail\nshut - shutdown")
    command = str(input(">"))
    if command == "yt" or command == "YT" or command == "не" or command == "НЕ":
        youtube()
    if command == "twitch" or command == "twich" or command == "TWITCH" or command == "TWICH" or command == "ецшеср" or command == "ецшср" or command == "ЕЦШЕСР" or command == "ЕЦШСР":
        twitch()
    if command == "zak" or command == "яфл":
        zak()
    if command == "mine" or command == "ьшту":
        mine()
    if command == "ds" or command == "вы":
        ds()
    if command == "gmail" or command == "пьфшд":
        gmail()
    if command == "shut" or command == "ырге":
        shutdown()
        
if __name__ == "__main__":
    main()
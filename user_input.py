from msvcrt import getch

# C:\Python27\python.exe C:/Users/mazmandian/PycharmProjects/Entrance/user_input.py

id_len = 6

last_char = ""
buf = ""

while True:
    last_char = getch()

    if ord(last_char) == 13:
        print "badge read refreshed"
        buf = ""
        continue

    buf += last_char
    if len(buf) == id_len:
        print "badge read: {}".format(buf)
        buf = ""

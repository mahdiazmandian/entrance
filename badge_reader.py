import subprocess, time, win32com.client as wincl, socket

port = 65432
addr = '127.0.0.1'


def send_badge_info(badge_id):
    s = socket.socket()
    s.connect((addr, port))
    s.send(badge_id)
    print "sent badge ID {}".format(badge_id)
    s.close()


mahdi_id = '6044779E'
katrine_id = 'C87FA30C'
nick_id = '6044779E'


def say_name_of_id(id_num):
    name = 'Guest'
    if id_num == mahdi_id:
        name = 'Matty'
    elif id_num == katrine_id:
        name = 'Katrin'
    elif id_num == nick_id:
        name = 'Nick'
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("Welcome {}".format(name))


while True:
    proc = subprocess.Popen('cmdpcprox -getactiveid  -waitforgetactiveid=3600', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
    s = proc.communicate()
    if not s[0]:
        print "Nothing Read"
    else:
        s = s[0]
        s = s.replace(" ", "")
        s = s[:8]
        print "Badge Read: {}".format(s)
        say_name_of_id(s)
        send_badge_info(s)
        # PROCESS BADGE DATA HERE
        # time.sleep(0.8)

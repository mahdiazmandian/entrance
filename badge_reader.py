import subprocess, time, win32com.client as wincl


mahdi_id ='6044779E'
katrine_id = 'C87FA30C'
nick_id = '6044779E'

def sayNameOfID (id):
    name = 'Guest'
    if id == mahdi_id:
        name = 'Matty'
    elif id == katrine_id:
        name = 'Katrin'
    elif id == nick_id:
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
        sayNameOfID(s)
        # PROCESS BADGE DATA HERE
        # time.sleep(0.8)

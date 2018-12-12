import subprocess, time

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
        # PROCESS BADGE DATA HERE
        time.sleep(1)

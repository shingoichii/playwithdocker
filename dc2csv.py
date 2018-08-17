#! /usr/bin/env python3
# c in csv == ':', not ','

def getportnumber (s):
    s1 = s.split('"')
    s2 = s1[1].split(':')
    return s2[0]

n = 0
readingportnumbers = 0
while True:
    try:
        s = input ()
        if readingportnumbers == 1:
            sshport = getportnumber (s)
            readingportnumbers = 2
        elif readingportnumbers == 2:
            webport = getportnumber (s)
            readingportnumbers = 3
        elif readingportnumbers == 3:
            applicationport = getportnumber (s)
            readingportnumbers = 0
        else:
            if s.find ('ports') > 0:
                readingportnumbers = 1
            elif s.find ('NEWUSERNAME') > 0:
                s1 = s.split('=')
                name = s1[1]
            elif s.find ('NEWPASSWORD') > 0:
                s1 = s.split('=', 1)
                pw = s1[1]
                print ("{}:{}:{}:{}:{}:{}".format (n, name, pw, sshport, webport, applicationport))
                n += 1
    except EOFError:
        break
 
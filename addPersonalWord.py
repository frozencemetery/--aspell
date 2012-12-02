#!/usr/bin/python
import sys

words = sys.argv[1:] # we take no options
if len(words) < 1:
  print("No words specified.")
  exit(1) # ick

import os

home = os.getenv("HOME")
locale = os.getenv("LANG")[:2]
personal = home + "/.aspell." + locale + ".pws"

pwsf = open(personal, 'r')
pwsc = pwsf.read().split('\n')[:-1]
pwsf.close()

for word in words:
  pwsc.append(word)

numl = pwsc[0].split(" ") # 3
numl[2] = str(int(numl[2]) + len(words))
pwsc[0] = " ".join(numl)

pwsf = open(personal, 'w')
pwsc = '\n'.join(pwsc) + '\n'
pwsf.write(pwsc)
pwsf.close()

exit(0) # success

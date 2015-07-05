#!/usr/bin/env python

import sys, time, getopt


def main(argv):
   inputfile = ''
   speed = '5'
   try:
      opts, args = getopt.getopt(argv,"hi:s",["ifile=", "speed="])
   except getopt.GetoptError:
      print 'typeprint.py --ifile <inputfile> --speed <1 - 5>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-s", "--speed"):
         speed = arg 
   wspeed = 0
   if speed == '1':
       wspeed = 0.5
   elif speed == '2':
       wspeed = 0.4
   elif speed == '3':
       wspeed = 0.3
   elif speed == '4':
       wspeed = 0.2
   elif speed == '5':
       wspeed = 0.1
   with open(inputfile, "r") as file:
     while 1 == 1:
       readnum = file.read(1)
       time.sleep(wspeed)
       sys.stdout.write(readnum)
       sys.stdout.flush()
       if not readnum:
         sys.exit()



main(sys.argv[1:])




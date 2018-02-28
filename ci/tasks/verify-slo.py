#!/usr/bin/python

import os

def write_error():
    f = open("slo-failure/message","w")
    f.write("Too many failures!")
    f.close() 

file = open("sli-value/total-time-results", "r")
samples = 0
failures = 0

line = file.readline()
while line:
    samples += 1
    if line.startswith("False"):
        failures += 1
    line = file.readline()

success_rate = 1 - (float(failures) / float(samples))

os.remove("sli-value/message")
if success_rate <= 0.99:
    write_error()

print "Success rate: " + str(success_rate)

# Here, you will write your task. Make sure that the task exits with a return code of 0 if
# successful and 1 (or some other non-zero) value if it fails!

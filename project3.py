# project3.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

from Scheduler import *
from time import sleep
import sys

def main():
    # Get the input file from the command line
    filename = sys.argv[1]
    sleepTime = int(sys.argv[2])
    batch = Scheduler()
    try:
        # Load the input line and start running the batch
        batch.load_jobs(filename)
        start(batch, sleepTime)
    except Exception as e:
        print(e)

def start(batch, sleepTime):
    running = True
    while running:
        try:
            running = batch.run()
            sleep(sleepTime)
        except KeyboardInterrupt:
            batch.halt()
    print("All jobs are completed. Exiting the program.")
    
if __name__=='__main__':
    main()
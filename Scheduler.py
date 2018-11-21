# Scheduler.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from Job import *
from Empty import *

class Scheduler:
    '''This class is a batch job scheduler that implements heap priority queue.''' 
    def __init__(self):
        self.__jobHeap = AdaptableHeapPriorityQueue()
    
    def load_jobs(self, filename):
        '''Loads jobs from input file.'''
        with open(filename, 'r') as file:
            for line in file:
                if not line.startswith('JOB,PRIORITY,LENGTH'):
                    data = line.rstrip().split(',')
                    job = Job(data[0], int(data[1]), int(data[2]))
                    self.__jobHeap.add((job.get_priority(), job.get_length()), job)
        file.close()
        
    def run(self):
        try:
            # Print current status
            current_key, current_job = self.__jobHeap.min()
            current_job.prnt_job()
            # Update
            if current_job.get_length() > 1:
                new_length = current_job.get_length() - 1
                current_job.set_length(new_length)
            else:
                self.__jobHeap.remove_min()
            return True
        except Empty:
            return False
    
    def halt(self):
        print("\nScheduler has been halted:")
        # Update the min with the remaining length
        current_key, current_job = self.__jobHeap.remove_min()
        self.__jobHeap.add((current_key[0], current_job.get_length()), current_job)
        
        # tmpHeap stores the job that is removed from the jobHeap
        tmpHeap = AdaptableHeapPriorityQueue()
        # nameDict is a dictionary that stores job names as keys and locators as values
        nameDict = {}
        # listJobs is a python list used to sort jobs
        listJobs = []        
        # prompt the user for how the table should be sorted
        srt = input("Sort by (j/p/l/h): ")
        print(self)
        try:
            while True:
                # Remove from jobHeap and print the job data if heap order is selected
                tmpKey, tmpJob = self.__jobHeap.remove_min()
                name = tmpJob.get_name()
                priority = tmpJob.get_priority()
                length = tmpJob.get_length()
                if(srt == 'h'):
                    print(tmpJob)
                # Add the job from the jobHeap to the tmpHeap
                nameDict[name] = tmpHeap.add(tmpKey, tmpJob)
                # Add the job to the listJobs
                listJobs.append((name, priority, length))
        except Empty:
            pass
        
        # Print the jobs based on the user input if other than heap order
        if srt == 'j':
            for j in sorted(listJobs, key=lambda jobs: jobs[0]):
                output = '{0:<20} '.format(j[0])
                output += '{0:>10} '.format(j[1])
                output += '{0:>10} '.format(j[2])
                print(output)
        elif srt == 'p':
            for j in sorted(listJobs, key=lambda jobs: jobs[1]):
                output = '{0:<20} '.format(j[0])
                output += '{0:>10} '.format(j[1])
                output += '{0:>10} '.format(j[2])
                print(output)
        elif srt == 'l':
            for j in sorted(listJobs, key=lambda jobs: jobs[2]):
                output = '{0:<20} '.format(j[0])
                output += '{0:>10} '.format(j[1])
                output += '{0:>10} '.format(j[2])
                print(output)
        
        # Add new job
        newJob = input("New job? (y/n): ")
        if newJob == 'y':
            name = input("New job name: ")
            priority = int(input("New job priority: "))
            length = int(input("New job length: "))
            newJob = Job(name, priority, length)
            tmpHeap.add((priority, length), newJob)
        # Alter a job
        alter = input("Alter priority? (y/n): ")
        if alter == 'y':
            name = input("Job name: ")
            priority = int(input("New priority: "))
            tmpKey, tmpJob = tmpHeap.remove(nameDict[name])
            tmpJob.set_priority(priority)
            tmpHeap.add((priority, tmpKey[1]), tmpJob)
        # Restart the scheduler
        print("Restarting scheduler...")
        self.__jobHeap = tmpHeap
            
    def __repr__(self):
        output = '{0:<20}  {1:>10}  {2:>10}'.format('Name', 'Priority', 'Length')
        output += '\n' + '-'*45 + '\n'
        return output
        
if __name__ == '__main__':
    print("Incorrect run format. Run project as python project3.py <input-job-listing> <sleep-time>")
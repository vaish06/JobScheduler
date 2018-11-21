# Job.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

class Job:
    '''A class representing jobs run by the scheduler class.'''
    def __init__(self, name, priority, length):
        self.__name = name
        if not isinstance(priority, int):
            raise TypeError('Priorities must be integers.')
        if priority < -20 or priority > 19:
            raise ValueError('Priorities must between -20 and 19')
        self.__priority = priority
        self.__length = length
        self.__total = length
    
    def get_name(self):
        return self.__name
    
    def get_priority(self):
        return self.__priority
    
    def get_length(self):
        return self.__length
    
    def get_total(self):
        return self.__total
        
    def set_name(self, name):
        self.__name = name
    
    def set_priority(self, priority):
        if not isinstance(priority, int):
            raise TypeError('Priorities must be integers.')
        if priority < -20 or priority > 19:
            raise ValueError('Priorities must between -20 and 19')
        self.__priority = priority
        
    def set_length(self, length):
        self.__length = length
    
    def __repr__(self):
        output = '{0:<20} '.format(self.__name)
        output += '{0:>10} '.format(self.__priority)
        output += '{0:>10} '.format(self.__length)
        return output
        
    def prnt_job(self):
        output = "Current job is '" + self.__name + "', "
        output += "priority " + str(self.__priority) + ','
        output += "iteration {0} of {1}.".format((self.__total - self.__length + 1), self.__total)
        print(output)

if __name__ == '__main__':
    print("Incorrect run format. Run project as python project3.py <input-job-listing> <sleep-time>")

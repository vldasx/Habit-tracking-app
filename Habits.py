#from datetime import timedelta # importing used module 

changing_freq = [1, 2, 3, 4, 5] # list of uneven intervals (in days) used for studying
 
class Habit:   
    """
    Class Habit describes the central figure in the program. 
    It has basic data (name, description) together with data needed for storing dates when habit is done. 
    
    Frequency variable has a double function: 
        
    1. for habits that are repeated in same intervals (any positive number can be used as number of days for repeating) 
    2. list of uneven intervals that is self repeated
    
    Number 0 is used to mark this second option. When 0 is selected, program uses frequency list stored in global 
    variable changing_freq. 
    Current streak is the last one unbroken chain of habit repeats. 
    """
    
    def __init__(self, name, description, frequency):  
         
        """ 
        habit is defined with 
        -name, 
        -description and 
        -frequency """ 
        
        self.name = name 
        self.description = description
        self.frequency = frequency
        self.checked = [] #  dates when habit has been done. User "checks" achieved habits
        self.current_streak = 0
        self.longest_streak = 0 
    
    
    def frequency_generator(self, counter): 
        """ returns adequate frequency for current loop """
        
        if self.frequency == 0: # variating frequency   
            if counter == len(self.checked): # last frequency + 1
                counter = 0              
            actual_freq = changing_freq[counter]
             
        else: # regular frequency
            actual_freq = self.frequency
            
        #print("counter", counter, "actual_freq", actual_freq)
        return actual_freq
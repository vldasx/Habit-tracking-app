""" 
Object Oriented and Functional Programming with Python
@author: Vladimir Miletin 91912710 
"""
from datetime import timedelta # importing used modules (datetime)

changing_freq = [1, 2, 3, 4, 5] # list of uneven intervals (in days) used for studying  


        
def current_and_longest_streak(self): 
    
    """ 
    /analytics are shown with data but calculated separately/
    
    Calculates current and longest streaks by looping through a list of dates "self.checked". Variable "previous_date" 
    holds the last date for the old cycle. The number of days in new cycle (frequency) added to "previous_date" is the second 
    date that is bound for that cycle. Var "difference" is the distance of tested date to "previous_date" in days.
    """
    
    self.current_streak = 1 # must be reseted before new calculation 
    self.longest_streak = 1
    print ("number of checked dates = ", len(self.checked))
    if len(self.checked) == 0: # habit not checked yet
        self.current_streak = 0 
        self.longest_streak = 0
        
    elif len(self.checked) == 1:
        """
        Habit only one time checked, both streaks are 1, already set"""
        pass
     
    else:
        difference = 0 # initialising difference 
        freq_counter = 0 # position in list changing_freq
 
        print(self.name, "  freq =",self.frequency, "day/s", ",last checked:", self.checked[-1]) # print info  
        
        """Other cases - more than 1 date are already checked """
        
        next_date = self.checked[0] + timedelta(days = self.frequency_generator(0))

        for x in range(1, len(self.checked)) : # iterates through checked dates list, begins with second date
            difference = (self.checked[x] - next_date).days # difference means "how far" is current date from bound
            
            if difference < 0: # within current range, ignore
                continue  
            
            elif difference > 0: # self.frequency_generator(freq_counter): 
                """
                Out of range, new streak.
                In case that this is last member of changing_freq list, function 
                frequency_generator will again return first member of that list."""
                
                self.current_streak = 1 # current date is first member in the streak
                freq_counter = 0       
                next_date = self.checked[x] + timedelta(days = self.frequency_generator(0)) # new test period ends at that day
                
            else: # the difference is within the current range!
                self.current_streak += 1  
                
                if freq_counter == len(changing_freq)-1:
                    freq_counter = 0 # when last, reset to begin (variating frequency)
                else:
                    freq_counter += 1  
                    
                next_date += timedelta(days = self.frequency_generator(freq_counter))# next test period
                      
                
            # checking if current streak is bigger than longest 
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak 
                
          
            
    print("current streak:", self.current_streak," longest streak:", self.longest_streak)  
    return  self.current_streak, self.longest_streak# return is here only for testing purposes

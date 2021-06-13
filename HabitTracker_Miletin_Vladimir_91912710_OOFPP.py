""" 
Object Oriented and Functional Programming with Python
@author: Vladimir Miletin 91912710 
"""
from datetime import  date, timedelta # importing used modules (datetime)
import os, json

learning_freq = [1, 2, 3, 4, 5] # list of uneven intervals (in days) used for studying  
new_habit = [] # stores all Habit class objects
 
class Habit:  
    """ Class Habit describes the central figure in program. It has basic data (name, description) together with 
    data needed for storing dates when habit is done. Frequency variable have a double function. First is for habits  
    that are repeated in same intervals (any positive number can be used as number of days for repeating) Second is for 
    list of uneven intervals that is self repeated. Number 0 is used to mark this second option. When 0 is selected, 
    program uses frequency list stored in global variable learning_freq. 
    Streak is continued no mater where the checked date is within the predefined boundaries. Current streak is the last 
    one unbroken chain of habit repeats. 
    """
    def __init__(self, name, description, frequency): 
        """ habit is defined with name, description and frequency """
        self.name = name 
        self.description = description
        self.frequency = frequency
        self.checked = [] #  dates when habit has been done. User "checks" achieved habits
        self.current_streak = 0
        self.longest_streak = 0 
    
    def frequency_generator(self, counter):
        """ returns adequate frequency for current loop"""
        
        if self.frequency == 0: # variating frequency   
            if counter == len(self.checked): # last frequency
                counter = 0              
            actual_freq = learning_freq[counter]
             
        else: # regular frequency
            actual_freq = self.frequency
            
        #print("counter", counter, "actual_freq", actual_freq)
        return actual_freq
        
    def current_and_longest_streak(self): # analytics are shown with data but calculated separately
        """ Calculates current and longest streaks by looping through a list of dates "self.checked". Variable "previous_date" 
        holds last date for old cycle. The number of days in new cycle (frequency) added to "previous_date" is the second 
        date that is bound for that cycle. Var "difference" is the distance of tested date to "previous_date" in days.
        """
        self.current_streak = 0 # must be reseted before new calculation 
        self.longest_streak = 0
        print (" len checked = ", len(self.checked))
        if len(self.checked) == 0: # habit only one time or not checked
            self.current_streak = 0 
            self.longest_streak = 0
        elif len(self.checked) == 1:
            self.current_streak = 1 
            self.longest_streak = 1
        else:
            self.current_streak = 1# for case when len(self.checked==2) and they are not in one streak
            self.longest_streak = 1
            #print("chk 1")    
            difference = 0 # start difference 
            freq_counter = 0 # position in list learning_freq
 
            print(self.name, "  freq =",self.frequency, "day/s", ",last checked:", self.checked[-1]) # print info  
            previous_date = self.checked[0] + timedelta(days = self.frequency_generator(0)-1)            
            """ Begin of first block of dates was self.checked[0], its bound is current frequency-1 days away from 
            the self.checked[0]. This -1 is because bound is last day of this cyclus """  
            for x in range(1, len(self.checked)) : # iterates through checked dates list, begins with second date
                difference = (self.checked[x] - previous_date).days # difference means "how far" is current date from bound
                #control_print("1st previous",previous_date, " difference=", difference)
                
                if difference <= 0: # within same range, ignore
                    continue  
                
                elif difference > self.frequency_generator(freq_counter): 
                    """Out of range, new streak. freq_counter is a new bound. In case that this is last member of 
                    learning_freq list, function frequency_generator will again return first member of that list."""
                    self.current_streak = 1 # current date is first member in the streak
                    freq_counter = 0       
                    previous_date = self.checked[x] + timedelta(days = self.frequency_generator(0)-1) # new test period ends at that day
                    
                else: # difference is within current range!
                    self.current_streak += 1  
                    
                    #print("chk4")
                    
                    if freq_counter == len(learning_freq)-1:
                        freq_counter = 0 # when last, reset to begin (variating frequency)
                    else:
                        freq_counter += 1  
                        
                    previous_date += timedelta(days = self.frequency_generator(freq_counter))# next test period
                    
                
                    
                # checking if current streak is bigger than longest 
                if self.current_streak > self.longest_streak:
                    self.longest_streak = self.current_streak 
                    
                control_print( " 2nd previous",previous_date, "current-", self.checked[x]) # control printing segment 
                control_print(" c.streak-",self.current_streak, "  longest.st.-", self.longest_streak)
                
        print("current streak:", self.current_streak," longest streak:", self.longest_streak)  
  

def control_print(a,b,c,d):
    """help for program testing, it is easily turned off when obsolete"""
    #print(a,b,c,d) # when this line turned to comment, function neutralized
    pass  


def load_and_create():
    """ Load habits from json file and creates habit class objects. Data contains no decreasing dates, but dates can be 
    repeated (many practices during one day or one week). 
    """
    with open('HabitTrackerData.json') as a:
        data = json.load(a)    
    
    for index, habit_data in enumerate(data, start=0):
        new_habit.append(Habit(habit_data['basic'][0], habit_data['basic'][1], habit_data['basic'][2]))
        
        for checked_date in habit_data['dates']:
            new_habit[index].checked.append(date(checked_date[0], checked_date[1], checked_date[2]))
            
            
def save_to_json(): 
    """ Saves all habits to json file. Json file contains main list of dictionaries, every dictionary for one habit. """   
    prepared_data = [] # stores data for export
    
    for index, habit_object in enumerate(new_habit): # prepare data to export 
        #print({"basic": [habit_object.name, habit_object.description, habit_object.frequency], "dates":[]})
        #print(type({"basic": [habit_object.name, habit_object.description, habit_object.frequency], "dates":[]}))
        prepared_data.append({"basic": [habit_object.name, habit_object.description, habit_object.frequency], "dates":[]})
        #pass
        for checked_date in habit_object.checked:
            prepared_data[index]["dates"].append([int(checked_date.year), int(checked_date.month), int(checked_date.day)])
            #print(int(checked_date.year), int(checked_date.month), int(checked_date.day))
           
            
    with open('HabitTrackerData.json', 'w') as a:
        json.dump(prepared_data, a, indent=2)   
        
def create_habit(): 
    """creates habit from user input"""
    print("Creating new habit:")
    new_habit.append(Habit(input("name:"), input("description:"), 
                     int(input("frequency in days or 0 for learning:"))))
    
def delete_habit(): 
    """ deleting whole habit"""
    delete = int(input("which habit to delete? (only real data, from number 3): "))
    if delete >= 3:
        del new_habit[delete]
    else:
        print("wrong number!")


def presenting_habits(): 
    """ Habits are presented together with analytics. There are test(first 3) and real data. """
    input_check = False   
    os.system('cls')
    while input_check == False:
        input_test_or_real =  input("test or real habits? t/r: ") 
        print()
        if input_test_or_real == "t":
            test_or_real = "TEST"
            begin = 0
            end = 3 # present test data
            input_check = True
        elif input_test_or_real == "r":
            test_or_real = "REAL"
            begin = 3 
            end = len(new_habit) # present real data
            input_check = True 
        else:             
            print("Please enter right value!")    
    print("THIS IS", test_or_real, "DATA")
    print("-----------------")
    
    # when checked today, analytics are calculated again for this habit
    for x in range(begin, end): 
        print("Habit number ",x)
        new_habit[x].current_and_longest_streak()
        print("-------------")        
    # checking todays work
    quit_check = False
    while quit_check == False:
        print()
        print("which habit have you finished today? Type number,")
        habit_input = input("or n for new habit, d delete, q for quit: ")
        if habit_input == "n":
            create_habit()
        elif habit_input == "d":
            delete_habit()
        elif habit_input == "q":
            quit_check = True
        else:          
            new_habit[int(habit_input)].checked.append(date.today())
            print("-----------------")
            new_habit[int(habit_input)].current_and_longest_streak()
            print("-----------------")
    return quit_check

# main program
    
load_and_create()
quit_check = False
while quit_check == False:
    quit_check = presenting_habits()
    
print("Saving data to file and quiting the program!")
  
save_to_json()








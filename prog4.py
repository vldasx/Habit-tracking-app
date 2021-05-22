""" 
Object Oriented and Functional Programming with Python
@author: Vlada
"""
from datetime import  date, timedelta # importing used modules (datetime)
import os

learning_freq =(1, 7, 30, 90, 180)
 
class habit:    
    def __init__(self, name, description, frequency):
        self.name = name 
        self.description = description
        self.frequency = frequency
        self.checked = []
        self.current_streak = 1
        self.longest_streak = 1 
    
    def frequency_generator(self, counter):
        if self.frequency == 0: #variable frequency    
            actual_freq = learning_freq[counter]
        else:
            actual_freq = self.frequency
        return actual_freq
        
    def current_and_longest_streak(self):# analytics are shown with data but calculated separately
        if len(self.checked) == 1:return 1,1 # only one member
        difference = 0 # start diference 
        freq_counter = 0
        #current_frequency = frequency_generator(0)
        self.current_streak = 1
        self.longest_streak = 1 
        print(self.name, "  freq =",self.frequency, "day/s", ",last checked:", self.checked[-1])#info  
        previous_date = self.checked[0]+ timedelta(days = self.frequency_generator(freq_counter))#first date 
           
        for x in range(1, len(self.checked)) : # iterate through checked dates list
            difference = (self.checked[x] - previous_date).days
            control_print("1st previous",previous_date, " difference=", difference)
            
            if difference < 0:# within same range, ignore
                continue  
            
            elif difference >= self.frequency: # out of range, new streak
                self.current_streak = 1
                freq_counter = 0       
                previous_date = self.checked[x] + timedelta(days = self.frequency_generator(freq_counter))# new test period  
                
            else: # difference is not in current range
                self.current_streak = self.current_streak + 1  
                freq_counter += 1
                if freq_counter == len(learning_freq)-1:
                    freq_counter = 0 # when last, reset to begin
                previous_date = previous_date + timedelta(days = self.frequency_generator(freq_counter))# next test period, avoid duplicates             
                
#control printing part, check if current is bigger than longest streak
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak # check if current streak is biggest               
            control_print( " 2nd previous",previous_date, "current-", self.checked[x]) 
            control_print(" c.streak-",self.current_streak, "  longest.st.-", self.longest_streak)        
        print("current streak:", self.current_streak," longest streak:", self.longest_streak)  
  
def control_print(a,b,c,d):
    #print(a,b,c,d)
    pass
     
# Data will not contain decreasing dates, but dates can be the same (many practices during one day)
new_habit = []  

new_habit.append(habit("0 test habit", "just running!", 1))
new_habit[0].checked = [date(2000,5,4), date(2000,5,5), date(2000,5,6), date(2000,5,7), date(2000,5,8),
                         date(2000,5,9), date(2000,6,6), date(2001,6,7), date(2001,6,9), date(2001,6,10),
                         date(2021,3,3), date(2021,3,6), date(2021,3,7), date(2021,5,16), date(2021,5,17)]

new_habit.append(habit("1 test habit", "7day", 7))
new_habit[1].checked = [date(2000,5,4), date(2000,5,5), date(2000,5,18), date(2000,5,19), date(2000,5,26), 
                         date(2000,5,27), date(2000,6,6), date(2001,6,7), date(2001,6,9), date(2001,6,10)]

new_habit.append(habit("2 test habit", "xxx", 0))
new_habit[2].checked = [date(2000,5,4), date(2000,5,5), date(2000,5,6), date(2000,5,7), date(2000,5,8), 
                         date(2000,5,9), date(2000,6,6), date(2001,6,7), date(2001,6,9),  date(2001,6,10)]

new_habit.append(habit("3 real variable habit", "always running!", 1))
new_habit[3].checked = [date(2000,5,4), date(2000,5,5), date(2000,5,6), date(2000,5,7), date(2000,5,8),
                         date(2000,5,9), date(2000,6,6), date(2001,6,7), date(2001,6,9), date(2001,6,10)]

def create_habit():
    print("Creating new habit:")
    new_habit.append(habit(input("name:"), input("description:"), 
                     int(input("frequency in days or 0 for learning:"))))
    
def delete_habit():
    delete = int(input("which habit to delete? (only real data, from number 3): "))
    if delete >= 3:
        del new_habit[delete]
    else:
        print("wrong number!")

def presenting_habits(): # choose between real and test data
    check2 = False  
    os.system('cls')
    while check2 == False:
        answer1 =  input("test or real habits? t/r: ") 
        print()
        if answer1 == "t":
            real_or_test = "TEST"
            begin = 0
            end = 3 # present test data
            check2 = True
        elif answer1 == "r":
            real_or_test = "REAL"
            begin = 3 
            end = len(new_habit) # present real data
            check2 = True
        else:             
            print("Please enter right value!")    
    print("THIS IS", real_or_test, "DATA")
    print("-----------------")
    for x in range(begin, end): 
        new_habit[x].current_and_longest_streak()
        print("-------------")        
    # checking todays work
    check1 = True
    check3 = True
    while check3 == True:
        print()
        print("which habit have you finished today? Type number,")
        habit_input = input("or n for new habit, d delete, q for quit: ")
        if habit_input == "n":
            create_habit()
        elif habit_input == "d":
            delete_habit()
        elif habit_input == "q":
            check1 = False
            check3 = False
        else:# without control, add if needend           
            new_habit[int(habit_input)].checked.append(date.today())
            print("-----------------")
            new_habit[int(habit_input)].current_and_longest_streak()
            print("-----------------")
    return check1

# main program
check1 = True
while check1 == True:
    check1 = presenting_habits()
        

    



    


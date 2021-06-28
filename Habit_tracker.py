""" 
Object Oriented and Functional Programming with Python
@author: Vladimir Miletin 91912710 
"""
from  analytics import current_and_longest_streak
import Habits
from datetime import  date # timedelta importing used modules (datetime)
import os, json
import logging

logging.basicConfig(filename="log_test.log", level=logging.DEBUG)
   
new_habit = [] # stores all Habit class objects

 

def load_and_create(): 
    """
    Load habits from json file and create habit class objects. 
    Data contains no decreasing dates, but dates can be 
    repeated (many times practicing during one day or one week). 
    """
    with open('HabitTrackerData.json') as a:
        data = json.load(a)    
    
    for index, habit_data in enumerate(data, start=0):
        new_habit.append(Habits.Habit(habit_data['basic'][0], habit_data['basic'][1], habit_data['basic'][2]))
        
        for checked_date in habit_data['dates']:
            new_habit[index].checked.append(date(checked_date[0], checked_date[1], checked_date[2]))        

 
 
def save_to_json(): 
    """ Saves all habits to json file. Json file contains a main list of dictionaries, every dictionary for one habit. """   
    prepared_data = [] # stores data for export
    
    for index, habit_object in enumerate(new_habit): # prepare data to export 
        prepared_data.append({"basic": [habit_object.name, habit_object.description, habit_object.frequency], "dates":[]})
        
        #logging.info('Save Json index {} '.format(index))
        for checked_date in habit_object.checked:
            prepared_data[index]["dates"].append([int(checked_date.year), int(checked_date.month), int(checked_date.day)])
                  
            
    with open('HabitTrackerData.json', 'w') as a:
        json.dump(prepared_data, a, indent=2)   
        
        
        
def analyse():
    """ 
    Shows all analytical data. When checked off today, 
    analytics are calculated again only for this habit """
    answer = ""
    print()
    print(" ------------------")
    print(" ANALYTICAL SEGMENT")
    print(" ------------------")

    while answer != "r":
        answer = input(" a for all streaks,\n o for one habit streaks or\n just type number for all habits with that periodicity \n or r for return: ")
        if answer == "a":
            print("\n\nALL STREAKS:\n")
            print("------------")
            analyse_loop(0, len(new_habit))
                
        elif answer == "o":
            answer = input("which habit: ")
            print("\n\nONE HABIT ANALYTICS:\n")
            print("-------------------")
            if not answer.isnumeric() or int(answer) > len(new_habit)-1 or int(answer) < 0:
                print("-----------------") 
                print("wrong input!")
                continue                
            print("Habit number ",answer)
            current_and_longest_streak(new_habit[int(answer)])
            continue
        
        elif answer.isnumeric():
            print("-----------------")
            print("Habits found that have", answer, "days cycle:\n--")
            for x in range(0, len(new_habit)): 
                if int(answer) == new_habit[x].frequency:
                    print("Habit number ",x)
                    current_and_longest_streak(new_habit[x])
                    print("-------------") 
        elif answer == "r":
            continue
        else:
            print("Try again!")
          
            
            
def analyse_loop(begin, end):
    """ 
    Shows all analytical data. When checked off today, 
    analytics are calculated again only for this habit """
    for x in range(begin, end): 
        print("Habit number ",x)
        current_and_longest_streak(new_habit[x])
        print("-------------") 
                

        
def create_habit(): 
    """creates habit from user input"""
    print("Creating new habit:")
    new_habit.append(Habits.Habit(input("name:"), input("description:"), 
                     int(input("frequency in days or 0 for learning:"))))
    print("Created!")
    
    
    
def delete_habit(): 
    """ deleting whole habit"""
    delete = int(input("which habit to delete? (only real data, from number 3): "))
    if delete >= 3 and delete < len(new_habit):
        del new_habit[delete]
        print("Deleted!")
        #logging.info("Deleted ", delete)
    else:
        print("wrong number!")

 

def presenting_habits(): 
    """ Habits are presented together with analytics. There are tests(first 3) and real data. """
    input_check = False   
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
       
    analyse_loop(begin, end)
          
    # checking todays work
    quit_check = False
    while quit_check == False: 
        print()
        print("which habit have you finished today? Type number from 3 to", len(new_habit),"or")
        habit_input = input("n for new habit \nd delete \na analyse  \nq for quit: ")
        
        if habit_input == "n":
            create_habit()
            
        if habit_input == "a":
            analyse()
            
        elif habit_input == "d":
            delete_habit()
            
        elif habit_input == "q":
            quit_check = True
            
        else:
            if not habit_input.isnumeric() or int(habit_input) > len(new_habit)-1 or int(habit_input) < 3:
                print("-----------------") 
                print("Wrong input, try again!")
                continue                
            new_habit[int(habit_input)].checked.append(date.today())
            print("-----------------")
            current_and_longest_streak(new_habit[int(habit_input)])
            print("-----------------")
        #logging.debug('Main choice ', habit_input)

    return quit_check

 

# main cycle 
def main():
    os.system('cls')
    print("\n \nWelcome to Habit Tracker v.2.1 \n \nTrack, maintain and support good habits!\n****************************************")
    load_and_create()
    quit_check = False
    while quit_check == False:
        quit_check = presenting_habits()
        
    print("Saving data to file and quitting the program!")
      
    save_to_json()


if __name__ == "__main__":
   # will run if not called as module thru import
   main()

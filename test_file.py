# -*- coding: utf-8 -*-
"""
Test module 
""" 

import Habits 
import Habit_tracker



test_habit1 = Habits.Habit("test name1", "test description1", 0)

""" this habit has several different frequencies, initial mark is 0 """


def test_frequency_generator1():
    """
    Tests frequency output for variable frequencies. 
    In case when third parameter of Habit instance (frequency) is equal 0
    it returns adequate frequency from the list."""
    
    assert test_habit1.frequency_generator(0) == 1
    assert test_habit1.frequency_generator(1) == 2
    assert test_habit1.frequency_generator(4) == 5
    
   
    
test_habit2 = Habits.Habit("test name2", "test description2", 2)

def test_frequency_generator2():
    """
    This habit has only one frequency (2), initial mark is 2
    when frequency_generator receives different numbers, must ignore them
    and return adequate frequency (2) """
   
    assert test_habit2.frequency_generator(0) == 2
    assert test_habit2.frequency_generator(1) == 2
    assert test_habit2.frequency_generator(4) == 2



Habit_tracker.load_and_create() 
def dates_length():
    """
    Makes sum of first 6 habits frequencies for test_load function"""
    
    total_lenght = 0
    for x in range(5):
        total_lenght += Habit_tracker.new_habit[x].frequency
    return total_lenght
         


def test_load_create():
    """
    compares different data points from internal data list which holds data 
    meant for processing. Those data has been loaded from JSON file."""
    
    assert Habit_tracker.new_habit[1].name == "long test habit"
    assert Habit_tracker.new_habit[1].description == "pairs "
    assert Habit_tracker.new_habit[1].frequency == 2

    assert Habit_tracker.new_habit[3].name == "long test habit"
    assert Habit_tracker.new_habit[3].description == "week "
    assert Habit_tracker.new_habit[3].frequency == 7
    
    assert dates_length() == 14 
    
 

def test_analyse_regular():
    """
    Compares current and longest streaks with data given by an analytical module.
    These are regular repeating periods."""
    
    assert Habit_tracker.current_and_longest_streak(Habit_tracker.new_habit[0]) == (1, 13)
    assert Habit_tracker.current_and_longest_streak(Habit_tracker.new_habit[1]) == (1, 12)
    assert Habit_tracker.current_and_longest_streak(Habit_tracker.new_habit[2]) == (1, 8)
    
    
    
def test_analyse_variating():
    """
    Compares current and longest streaks with data given by analytical module,
    with variating periods."""
    
    assert Habit_tracker.current_and_longest_streak(Habit_tracker.new_habit[5]) == (1, 8)


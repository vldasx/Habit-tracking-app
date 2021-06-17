# Habit-tracking-app

Development/reflection phase

This is a small habit tracker with a very simple user interface. 

Habit tracking can be used in daily life as a control mechanism, or for attempts to establish new healthy habits.


1. Package content:


Habit tracking app consists of two groups of files: first is group is for regular users:
- HabitTracker_Miletin_Vladimir_91912710_OOFPP.exe this is the main program that is executable, meaning that no python or other programs need to be installed in order for him to work.
- HabitTrackerData.json which contains data necessary for this program. All changed data will be saved at the end again in this file.  Those files must be in the same folder, and no particular maintenance is needed. This is tested for Windows. These two files are sufficient for program usage. 

There are  “Developer” files which are python versions of exe file, and they are open for inspection, testing and changes. These files are 
- HabitTracker_Miletin_Vladimir_91912710_OOFPP.py - main program in python
- HabitTracker_test_data_generator.py - this is a small help program for generating data sets for testing, or preparing data from the previous period and other habits for the main program. This program will create a json file.
- HabitTrackerData.json - this is the same data file as the first group above, json storage of data.


2. Plain user instructions:

Clone the repo !!!
https://github.com/vldasx/Habit-tracking-app/blob/main/HabitTracker_Miletin_Vladimir_91912710_OOFPP.exe  and
https://github.com/vldasx/Habit-tracking-app/blob/main/HabitTrackerData.json 

![image](https://user-images.githubusercontent.com/38176126/121818513-fe0f5100-cc87-11eb-99d0-8b9b674f2bd3.png)

and put them in the same folder. Run the exe file. The window will open, and it is ready to go. First three habits are test data and they will be shown when “t” is chosen as shown in the picture. This is also the main switchboard, all the possibilities are shown here. After every update of the finished habit, fresh data for this habit will be calculated and displayed.


	

2.2 Developer / tester instructions:

Clone the repo
https://github.com/vldasx/Habit-tracking-app/blob/main/HabitTracker_Miletin_Vladimir_91912710_OOFPP.py  ,
https://github.com/vldasx/Habit-tracking-app/blob/main/HabitTrackerData.json  and
https://github.com/vldasx/Habit-tracking-app/blob/main/HabitTracker_test_data_generator.py 
and put them in the same folder. Run python programs (HabitTracker and HabitTracker_test_data_generator). Behaviour of the program is the same as described. Test data generator have raw data sets that are useful for preparing test sets. The list contains all dates in one row one after another, allowing the user/tester to arrange and group dates for better clarity. Also, it is possible to comment out unused data by selecting those rows and pressing ctrl+1 (or uncomment them the same way). No additional steps are needed, HabitTrackerData.json will be created when running this python script. 

![image](https://user-images.githubusercontent.com/38176126/121819203-1c774b80-cc8c-11eb-83b0-2459bff13cc4.png)

HabitTracker_test_data_generator.py on the picture above shows how data is organized and commented. Simple # comment is chosen because it does not trigger indentation checking, allows additional commenting that will be ignored by exporting and it is easily done for multiple lines (ctrl+1). Here is a case where repeating frequency is 2 days, so the data is organized accordingly in pairs. Comment down-right marks 10 pairs, so it is easily compared with the program output. Picture under is for changing frequencies. Comments are used to mark important positions. Those comments will not obstruct JSON data in any way.

![image](https://user-images.githubusercontent.com/38176126/121819283-7d9f1f00-cc8c-11eb-9d9c-5c337896cc34.png)


	



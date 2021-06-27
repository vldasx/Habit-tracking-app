# Habit-tracking-app

This is a small habit tracker with a very simple user interface.
Habit tracking can be used in daily life as a control mechanism, or for attempts to establish new healthy habits.

Package content:
Habit tracking app consists of two groups of files, first is group is for regular users:
Habit_tracker.exe is the main program that is executable in Windows, meaning that no python or other programs need to be installed in order for it to work.
HabitTrackerData.json which contains data necessary for this program. All changed data will be saved at the end again in this file. Those files must be in the same folder, and no particular maintenance is needed. This is tested for Windows. These two files are sufficient for program usage.
There are “Developer” files which are python versions of exe file, and they are open for inspection, testing and changes. These files are
Habit_tracker.py - main program in python
Habits.py - Habits class
analytics.py - analysing segment
sample_test_generator.py - this is a small help program for generating data sets for testing, or preparing data from the previous period and other habits for the main program. This program will create a json file.
HabitTrackerData.json - this is the same data file as the first group above, json storage of data.
test_file.py - pytest testing module
 
Plain user instructions:
Clone the repo / download zip https://github.com/vldasx/Habit-tracking-app with files https://github.com/vldasx/Habit-tracking-app/blob/main/Habit_tracker.exe and https://github.com/vldasx/Habit-tracking-app/blob/main/HabitTrackerData.json
and put those files in the same folder. Run the Habit_tracker.exe file. The window will open, and it is ready to go. 
First three habits are test data and they will be shown when “t” is chosen as shown in the picture. “r” is for all other, i.e. “work” habits. 

![image](https://user-images.githubusercontent.com/38176126/123511976-094d7e00-d685-11eb-8308-71d1affedd07.png)

 
This is also the main switchboard, most of the possibilities are shown here. After every update of the finished habit, fresh analytics for this habit will be calculated and displayed.

![image](https://user-images.githubusercontent.com/38176126/123544785-23ef2800-d755-11eb-819d-509ece5ec098.png)


It is possible to make a new habit by entering “n”, one can be with “d” deleted, and "a" will give analytical menu.

![image](https://user-images.githubusercontent.com/38176126/123544818-5862e400-d755-11eb-9dd0-13d6b87d16aa.png)

In analytical segment is possible to get streaks for all habits "a", for one habit "o" and all habits with chosen periodicity simply by typing a number of days or 0.

Developer / tester instructions:
 
Clone the repo / download zip https://github.com/vldasx/Habit-tracking-app and put all files in the same folder. Run the previously installed python IDE (Spyder, PyCharm) and open Habit_tracker.py, which is a main file. This file will import all the data from HabitTrackerData.json. There is a convenient way to create a desirable data set for testing purposes, and that is by using sample_test_generator.py with has raw data sets that are useful for preparing test sets. The list contains all dates in one row one after another, allowing the user/tester to arrange and group dates for better clarity. Also, it is possible to comment out unused data by selecting those rows and pressing ctrl+1 (or uncomment them the same way). No additional steps are needed, HabitTrackerData.json will be created when running this python script.

![image](https://user-images.githubusercontent.com/38176126/123512019-4a459280-d685-11eb-85df-e2e4baed7a34.png)


HabitTracker_test_data_generator.py on the picture above shows how data is organized and commented. Simple # comment is chosen because it does not trigger indentation checking, allows additional commenting that will be ignored by exporting and it is easily done for multiple lines (ctrl+1). Here is a case where repeating frequency is 2 days, so the data is organized accordingly in pairs. Comment down-right marks 10 pairs, so it is easily compared with the program output. Picture below is data  with changing frequencies. Comments are used to mark important positions. Those comments will not obstruct JSON data in any way.

![image](https://user-images.githubusercontent.com/38176126/123512042-6fd29c00-d685-11eb-81b4-1e4485ba2785.png) 

Data from analyse function is set by the sample_test_generator data. This is data set number 5 which has freq value 0, meaning it has variable periods for habit. It is 
little trickier to calculate than regular repeating period that has only one number for frequency. Dates are splitted for convenience, allowing easy checking and testing.
Periodicity here is 1, 2, 3, 4, 5 days and than again from beginning. It can be seen from physical arrangement of data.

![image](https://user-images.githubusercontent.com/38176126/123512334-21260180-d687-11eb-9fcb-46ea66fe2b78.png)



Program testing:

To conduct testing, pytest must be installed (see https://docs.pytest.org/en/6.2.x/getting-started.html). Tests work with data in package.

![image](https://user-images.githubusercontent.com/38176126/123512052-87aa2000-d685-11eb-8e67-ff7e655c3d51.png)

Spyder has a possibility to conduct tests by click on Run (here-Ausführen) / Run unit tests. Another possibility is to type “pytest” in the shell which is pointed to a folder with files. It will also read and conduct a series of tests saved in test_file.py. Spyder will show results in the right window as in the picture.

![image](https://user-images.githubusercontent.com/38176126/123512062-95f83c00-d685-11eb-97cf-8e8db1db6ae2.png)

 






	



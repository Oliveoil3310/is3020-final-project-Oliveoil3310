# IS 3020 Final Project

## Student and Project Information

- Student name: Josh Oliverio
- GitHub username:Oliveoil3310
- Project title: Motorcycle Maintenance and Ride Tracker
- Application purpose: 
For my final project, I decided to create a Motorcycle Maintenance and Ride Tracker. I chose this project because I enjoy riding motorcycles and currently own a 2005 Kawasaki ZX6R. I wanted to create something that could actually be useful to me instead of just making a random program for an assignment.

The purpose of this application is to help motorcycle owners keep track of their motorcycle's mileage, maintenance history, upcoming services, and overall expenses. It can be easy to forget when certain maintenance was completed or how much money has been spent on a motorcycle. This program helps organize that information in one place.

The application uses a menu system that allows users to enter their motorcycle information, update their mileage, record maintenance, and track expenses. It also saves the information so users don't have to enter everything again each time they run the program.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.
To run this program, you will need Python 3.10 or newer and an application such as PyCharm.

Download or clone the project repository from GitHub.

Open the project folder in PyCharm.

Locate the Python file named motorcycle_tracker.py.

Right-click the file and select Run 'motorcycle_tracker'.

The program will display a menu with nine options.

Select option 1 to enter your motorcycle's year, make, model, and current mileage.

Use the other menu options to update mileage, record maintenance, and track expenses.

Select option 8 to save your information or option 9 to save and exit.

The program does not require any additional Python libraries to be installed because it uses built-in Python modules.
## Major Features

List the major user-facing features implemented in the final application.
Motorcycle Information

Users can enter their motorcycle's year, make, model, and current mileage. This information is saved and displayed when the program runs.

2. Mileage Tracking

Users can update their motorcycle's mileage as they continue riding. The program also prevents users from entering a mileage lower than the current recorded mileage.

3. Maintenance Records

The application allows users to record maintenance such as oil changes, chain maintenance, tire replacements, and other repairs. Each record includes the service performed, date, mileage, and cost.

4. Maintenance Reminders

Users can enter how many miles should pass before a service is needed again. The program calculates the next service mileage and lets users know when maintenance is coming up or overdue.

5. Maintenance History

Users can view previous maintenance records to see what work has already been completed on their motorcycle.

6. Expense Tracking

The program allows users to record expenses such as fuel, replacement parts, accessories, and other motorcycle-related purchases.

7. Total Expense Calculation

The application calculates the total amount spent on maintenance and other motorcycle expenses.

8. Saving Information

The application saves motorcycle information, maintenance records, and expenses into CSV files. This allows users to close the program and access their saved information when they open it again.
## Python Concepts Used
Throughout this project, I used several Python concepts that we learned during the semester.

Variables and Data Types: Variables are used to store motorcycle information, mileage, maintenance costs, and other values.

Conditional Statements: If, elif, and else statements are used to control the menu and determine when maintenance is due.

Loops: While loops keep the program running until the user chooses to exit. For loops are used to display records and calculate expenses.

Functions: I created separate functions for adding motorcycle information, updating mileage, recording maintenance, checking maintenance reminders, and calculating expenses.

Lists and Dictionaries: Lists and dictionaries are used to organize motorcycle information, maintenance records, and expense data.

File Handling: The program uses CSV files to save information and load it again when the application starts.

Exception Handling: Try and except statements help prevent the program from crashing when users enter invalid information or when certain file errors occur.

Modules: The program uses Python's built-in csv, pathlib, and datetime modules.
Explain how the application uses functions, collections, conditionals, loops, file persistence, and exception handling.

## Data Files

Describe each CSV or JSON file and provide a brief explanation of its fields.
The application uses three CSV files to store information.

motorcycle.csv

Stores the motorcycle's year, make, model, and current mileage.

maintenance.csv

Stores maintenance dates, service descriptions, mileage, costs, and the mileage when the next service is due.

expenses.csv

Stores motorcycle expenses, including dates, descriptions, categories, and amounts spent.

These files are created automatically when information is saved through the program.
## Testing Summary

Describe the major scenarios tested, including invalid input and file-related errors.
I ran the application in PyCharm to make sure the Python code executed and the main menu appeared correctly.

For my motorcycle information, I used the following details:

Year: 2005

Make: Kawasaki

Model: ZX6R

Current Mileage: 28,000 miles

The application is designed to validate user input, save records into CSV files, and calculate upcoming maintenance and total expenses.

Additional tests include checking that mileage cannot decrease, confirming that maintenance reminders calculate correctly, and verifying that saved information loads when the program is restarted.
## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.
# AI Usage Documentation

## AI Tool Used

AI assistance was used during the development of my Motorcycle Maintenance and Ride Tracker.

## How AI Was Used

I used AI as a resource to help troubleshoot problems, make adjustments, and improve the overall functionality of my motorcycle tracker. It helped me understand how different parts of the Python program worked together and identify ways to make the code more organized and easier to follow.

AI also assisted with developing and refining the program's functions, including the menu system, maintenance reminders, expense calculations, and CSV file handling.

## Most Important AI-Assisted Improvements

**1. Code Organization:** AI helped divide the program into separate sections and functions, making the code easier to read, troubleshoot, and update.

**2. Error Handling:** AI assisted with improving input validation so the program could handle incorrect entries without immediately crashing.

**3. Maintenance Tracking:** AI helped refine the mileage calculations used to determine when maintenance is coming up, due, or overdue.

**4. Saving Information:** AI helped improve how motorcycle information, maintenance records, and expenses are saved and loaded using CSV files.

**5. Troubleshooting:** AI provided guidance for identifying problems and running the application correctly in PyCharm.

## Testing and Review

I reviewed the program in PyCharm and ran it to confirm that the application launched and displayed the menu correctly. I also used my 2005 Kawasaki ZX6R with 28,000 miles as an example when working with the program.

AI was a helpful resource for making improvements, understanding the code, and working through issues during development.
The most important improvements AI assisted with were organizing the code into sections, improving error handling, and making the maintenance tracking and expense calculations work more effectively. AI also helped improve how information was saved using CSV files and provided troubleshooting guidance when running the program in PyCharm. These improvements made the motorcycle tracker easier to use, more organized, and more reliable.
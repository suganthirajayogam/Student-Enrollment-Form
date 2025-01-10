# Student-Enrollment-Form


##Description:
This project is a simple graphical user interface (GUI) registration form built using Tkinter, which allows users to enter personal details such as name, mobile number, email ID, course preferences, batch selection, and more. The form is designed for Besant Technologies, and the data entered can be displayed in the console upon submission.

Technologies Used:
Python: Programming language used to develop the application.
Tkinter: Python's built-in library for creating graphical user interfaces.
PyMySQL (optional): A Python library for connecting to and interacting with a MySQL database. This part is optional and can be added to store form data in a database.
Requirements:
To run the application, ensure you have Python and Tkinter installed. If you plan to integrate with a MySQL database, you will also need the PyMySQL library.

Python 3.x: Python is required to run the project.
Tkinter: Tkinter is included with Python. If not installed, you can install it using the following command:
Copy code
pip install tk
PyMySQL (optional, for database integration):
Copy code
pip install pymysql
Features:
User can input personal details such as name, mobile number, email ID, and address.
Course and batch preferences can be specified.
The application uses Tkinter to display the form in a user-friendly GUI.
Upon submission, the entered details are printed in the console (this is where you can add database functionality to save the data using PyMySQL).
How to Run the Application:
Download or clone the project to your local system.
Open a terminal or command prompt and navigate to the project folder.
Run the Python script to start the Tkinter form:
Copy code
python registration_form.py
The registration form will appear, allowing you to input details and click the "Submit" button to see the entered data printed in the console.
Example Usage:
Personal Details: Enter your name, mobile number, alternate number, email ID, etc.
Course Preferences: Select the course you're interested in.
Batch Preferences: Choose your preferred batch.
After filling out the form, click Submit, and the data entered will be displayed in the terminal.
Database Integration (Optional):
If you want to store the form data in a MySQL database, you can use the PyMySQL library to connect to your database and insert the data. This integration is optional and not included in the current script. Below is a general guide on how to set up the database integration:

Example Database Code (not included in the script):
Use PyMySQL to connect to your MySQL database and save form data into a table.
Future Enhancements:
Database Integration: Implement code to save form data into a MySQL database.
Input Validation: Add validation for the entered data, such as ensuring the mobile number and email address are valid.
Improved GUI: Enhance the GUI with dropdown menus, radio buttons, and other interactive elements to improve user experience.
License:
This project is open-source and free to use for educational purposes.

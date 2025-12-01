# Life Style and My Expenses Project Overview 

This README file provides an outline of a project using the Life Style and My Expenses dataset. The project includes data cleaning, database creation, and a web application to visualize the data. 

## Dataset Information 
The dataset used for display on the homepage for this project can be found on Kaggle: [Life Style Data]( https://www.kaggle.com/datasets/jockeroika/life-style-data)

The dataset used for adding and filtering items into the database for this project can be found on Kaggle: [Personal expense dataset]( https://www.kaggle.com/datasets/sanjay3454chauhan/personal-expense-data). 


**Step 1: Data Cleaning**

*Steps: Data Cleaning Life Style Data*
Steps:
- Duplicate & Missing Value Check 
there was no missing values or missing values
- Remove Redundant Features
	8 Columns was removed because data was redundant 
- Data Consistency Validation
	1 column was drop because of in consistent data in field.
- Create Derived Variables
	1 column used for the age column 
- Transform & Convert Types
	3 column was converted from float to integer 
- Standardize column names
	Converted column names into a standardized form.

*Steps: Data Cleaning Personal Expense Dataset*
Steps:
- Duplicate & Missing Value Check
	there was no missing values or missing values.
- Remove Redundant Features
	there were no redundant features. 
- Data Consistency Validation
Data that did not adhere to data convention was eliminated- due to user error


**Step 2: Database Creation** 

The cleaned data is read from 'new_Life_Style_Data.cvs' and 'new_myExpenses csv' by the 'databases_SL.ipynb' and 'databases_ME.ipynb' script, which then loads it into an SQLite database respectively.  
 
**Step 3: Web Application** 

The Flask framework is used by the 'app.py' script to build a web application with six routes: 

- **/**: The 'home.html' is default page (Homepage).
- **/about_life_style**: The 'about_life_style.html' page states information about the Life Style dataset. 
- **/life_style_sample_dataset**: The ' life_style_sample_dataset.html' page displays 200 rows of the Life Style dataset. 
- **/about_my_expenses**: The 'about_my_expenses.html' page states information about the My expenses dataset. 
- **/about_life_style**: The 'about_life_style.html' page states information about my expenses dataset and allow the user to filter the dataset.
- **/submit**: Opens the 'submit.html' page allows user to add data into my expenses database.


## Explanation of the Website  

- All pages will use the theme_style.css to ensure uniformity of style.

- All pages except /life_style_sample_dataset has a  navigator to the left side of page.  

- The navigator contains six routes:

1.	Homepage (home.html) page states the contributors of the DAB111 - Group 6 Project and access to our LinkedIn page. 

2.	About Life Style dataset (about_life_style.html) explains briefly intro to dataset with a link to the original dataset and a description of each variable. 

3.	Life Style Sample Dataset (life_style_sample_dataset.html) display only 200 rows of dataset with a button to return to homepage.

4.	About My Expenses dataset (about_my_expenses.html) explains brief intro to dataset with a link to the original dataset and a description of each variable. 

5.	My Expenses Dataset (filter_my_expenses_dataset.html) display of data with ability to filter dataset.

6.	Add data to Expenses Dataset (submit.html) used to add data into the dataset.
 

## How to Experience the Journey 

1.	Prerequisites
Make sure the following software is installed on your system:
- Python 3.x
- pip (Python package manager)
- Git
- virtualenv 

2. 	Clone this repository to your local machine <br>
- Option 1 - Download ZIP: <br>
Download the project as a ZIP file from GitHub and extract it to your preferred location. <br>
- Option 2 - Clone using Git: <br>
Open a terminal and run the following commands: <br>
git clone https://github.com/Nilari-BD/DAB111_group_6.git <br>
cd DAB111_group_6 <br>

2.5. Alternative step: Create and Activate a Virtual Environment <br>
python3 -m venv venv <br>
venv\Scripts\activate <br>

3.	Navigate to the main folder
4.	Install the required package by running pip install -r requirements.txt
5.	Execute the Flask application by running python app.py in the terminal
6.	Access the website by going to http://127.0.0.1:5000/ or http://localhost:5000/ in your web browser.

  
**Note:** 

Feel free to explore the web application, and don't hesitate to contact us if you have any questions or run into any problems! 
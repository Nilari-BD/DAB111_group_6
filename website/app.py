from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

app = Flask(__name__)

# this is the default page 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about_life_style')
def about_life_style():
    return render_template('about_life_style.html')

@app.route('/about_personal_expenses')
def about_personal_expenses():
    return render_template('about_personal_expenses.html')

@app.route('/life_style_sample_dataset')
def life_style_sample_dataset():
    conn = sqlite3.connect('database/Life_Style_DB.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM Life_Style_table LIMIT 200')
    data = cursor.fetchall()
    headings = [description[0] for description in cursor.description]

    return render_template('life_style_sample_dataset.html', headings=headings, data=data)

@app.route('/submit', methods=['GET', 'POST'])
def submit():

    if request.method == 'POST':
        # Process form data only when a POST request is received
        date = request.form.get('date')
        item = request.form.get("item")
        amount = request.form.get('amount')
        category = request.form.get("category")
        time = request.form.get("time")        

        if not date: #not variable check empty and None
            # Handle the case where date is missing, e.g., display an error, use a default value, etc.
            return "Date not provided! Please go back and try again"
        elif not item: #not variable check empty and None
            # Handle the case where item is missing, e.g., display an error, use a default value, etc.
            return "Item not provided! Please go back and try again"      
        elif not amount: #not variable check empty and None
            # Handle the case where amount is missing, e.g., display an error, use a default value, etc.
            return "Amount not provided! Please go back and try again"
        elif not category: #not variable check empty and None
            # Handle the case where category is missing, e.g., display an error, use a default value, etc.
            return "Category not provided! Please go back and try again"
        elif not time: #not variable check empty and None
            # Handle the case where time is missing, e.g., display an error, use a default value, etc.
            return "Time not provided! Please go back and try again"    
        else:
            # Add values into database
            conn = sqlite3.connect('database/PersonalExpenses_DB.db')
            cursor = conn.cursor()
            
            cursor.execute(
                "INSERT INTO PersonalExpenses_table VALUES (?, ?, ?, ?, ?, ?);", 
                (
                    date,
                    item,
                    float(amount),
                    category,
                    time,
                    datetime.strptime(date, "%Y-%m-%d").strftime("%A"),
                ),
            )

            conn.commit()
            return "Success! Your information has been received. Thank you."
    else:
        # Render the form template for GET requests            
        return render_template('submit.html')

@app.route('/filter_personal_expenses_dataset', methods=['GET', 'POST'])
def filter_personal_expenses_dataset():

    conn = sqlite3.connect('database/PersonalExpenses_DB.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM PersonalExpenses_table')
    data = cursor.fetchall()
    headings = [description[0] for description in cursor.description]

    filtered_data = data  # Start with all data
    search_query = ""

    if request.method == 'POST':
            search_query = request.form.get('search_query', '').lower()
            if search_query:
                #item[0] is Date; item[1] is Item; item[3] is Category; item[5] is day
                filtered_data = [item for item in data if search_query in item[0] or search_query in item[1].lower() or search_query in item[3].lower() or search_query in item[5].lower()]
    return render_template('filter_personal_expenses_dataset.html', headings=headings, data=filtered_data, search_query=search_query)    

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create a connection to SQLite database
def create_connection():
    conn = sqlite3.connect('vaccine_data.db')
    return conn

# Function to create a table to store user data if not exists
def create_table(conn):
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS vaccinations (
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            aadhar_no INTEGER primary key NOT NULL,
            vaccine_type TEXT NOT NULL,
            dose TEXT NOT NULL
        );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

# Route to display the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        email = request.form['email']
        aadhar_no = int(request.form['aadhar_no'])
        dose = int(request.form['dose'])
        vaccine_type = request.form['vaccine_type']

    
        
        # Insert data into the database
        conn = create_connection()
        with conn:
            create_table(conn)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vaccinations (name, age, email, aadhar_no, dose, vaccine_type) VALUES (?, ?, ?, ?, ?, ?)",
                           (name, age, email, aadhar_no, dose, vaccine_type))
            conn.commit()

        # Display form entries in the console using SQLite3
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vaccinations")
            rows = cursor.fetchall()

            if rows:
                print("Form entries:")
                print(rows)

        
    n=1
    if dose==1:
        if age<15:
            n = n+5
            comeback=(f'Please comeback after {n} months for your next dose')
        elif age<20:
            n= n+2
            comeback=(f'Please comeback after {n} months for your next dose')
        else:
            comeback = ''
        
    else:
        comeback = ''

    return redirect(url_for('success', name=name, age=age, email=email, aadhar_no=aadhar_no, dose=dose, vaccine_type=vaccine_type, comeback=comeback))


# Route to display success message along with user entries
@app.route('/success')
def success():
    name = request.args.get('name')
    age = request.args.get('age')
    email = request.args.get('email')
    aadhar_no = request.args.get('aadhar_no')
    dose = request.args.get('dose')
    vaccine_type = request.args.get('vaccine_type')
    comeback = request.args.get('comeback')

  
    
    

    return render_template('success.html', name=name, age=age, email=email, aadhar_no=aadhar_no, dose=dose, vaccine_type=vaccine_type, comeback=comeback)



if __name__ == '__main__':
    app.run(debug=True)
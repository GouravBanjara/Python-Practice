import sqlite3
conn = sqlite3.connect('ab.db')
c = conn.cursor()
try:
    c.execute('''create table IF not exists covid
              (name text,
               Aadhar_No integer primary key not null,
               Age int,
               Email varchar,
               Address varchar)''')

    def data_entry(name, aadharno, Age, Email, Vaccine):
        c.execute('insert into covid values(?,?,?,?,?)',(name, aadharno, Age, Email, Vaccine ))
        conn.commit()

    print()
    print("Hello User, Welcome to the Covid Vaccination program")
    print()
    print('Please fill the following details to get vaccinated')
    print()

    name = input('Name:' )
    aadharno = int(input('Aadhar No:' ))
    Age = int(input('Age:' ))
    Email = input('Email Id:' )
    print()

    print('Now please select the vaccine No. among these three available')
    print('1.Pfizer')
    print('2.Moderna')
    print('3.HVL')
    print()


    for i in range(100):
        Vaccine = int(input('Vaccine No:' ))
        print()
        if Vaccine == 1:
            print('You have selected Pfizer')
            break
        elif Vaccine == 2:
            print('You have selected Moderna')
            break
        elif Vaccine == 3:
            print('You have selected HVL')
            break
        else:
            print('Plese Enter 1,2 or 3 to select the vaccine')




    data_entry(name, aadharno, Age, Email, Vaccine)

    print()
    print(f'Thank you {name} for getting vaccinated and being a responsible citizen of our country')
    print()
    
    c.execute('Select * from covid')
    print(c.fetchall())

    conn.close()
    
   

except ValueError:
    print('Plese enter numerical value only for Aadhar no and Age')
except sqlite3.IntegrityError:
    print('Your Aadhar no. have already been registered')
    print(f'Thank you {name} for getting vaccinated and being a responsible citizen of our country')


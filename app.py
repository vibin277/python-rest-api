from flask import Flask,render_template,request
import sqlite3 as sql


app =Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/EnterNew')
def new_student():
    return render_template('Student.html')  


@app.route('/add',methods=['POST','GET'])
def addrec():
    if request.method=='POST':
        try:
          nm = request.form['nm']
          addr = request.form['add']
          city = request.form['city']
          pin = request.form['pin']
  
       
          with sql.connect("database.db") as con:

            cur =con.cursor()

            cur.execute("INSERT INTO students(name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))

            con.commit()

            msg = "RECORD SUCCESSFULLY ADDED"
        except:
            con.rollback()
            msg="Error in insert operation"

        finally:
            return render_template("result.html",msg=msg)  
            con.close()
            

if __name__=='_main_':
    app.run(debug=True)
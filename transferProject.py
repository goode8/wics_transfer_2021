import sqlite3 as sql
from flask import Flask, render_template, request
#from topColleges import TopCollege
# from flask import Blueprint     # For testing Blueprint creation here

# bp = Blueprint('main', __name__)    # Blueprint object (Leaving this out for now)

transferProject = Flask(__name__)   # Should this remain here ??


@transferProject.route('/')          # Switched to @bp.route() from @transferProject.route() <- Switched back
def first():
    return render_template('wicsProject.html')


@transferProject.route('/second', methods=['POST', 'GET'])   # Switched back to @transferProject.route() fro @bp.route()
def second():
   # if request.method == 'POST':
    #    college_list = TopCollege()
    #return render_template('transferlist.html', list=college_list)      # Switched from College List.html
    db = sql.connect("schools.db")  # Switched from transfer.db to colleges.db to test
    if request.method == 'POST':
        college_list = db.execute("SELECT * FROM alluniversityinfo ORDER BY(rank) ASC NULLS LAST")
        return render_template('transferlist.html', list=college_list)
    db.close();

@transferProject.route('/third', methods=['POST', 'GET'])          # Switched to @bp.route() from @transferProject.route() <- Switched back
def third():
    #try:
         #(id INTEGER, rank INTEGER, college TEXT, city TEXT, state TEXT, tuition TEXT, admission_rate TEXT, student_population TEXT, website TEXT, course_equivalency TEXT, transfer_page TEXT, career_services TEXT, public_private TEXT, SAT_Reading_Writing TEXT, SAT_Math TEXT, ACT_English TEXT, ACT_Math TEXT, international_students TEXT, UG_men TEXT, UG_women TEXT);
        con = sql.connect('schools.db')
        print ("Opened database successfully")
        cur = con.cursor()
        cur.execute("select * from alluniversityinfo where \"INSTNM\"=" + "\"" + request.args.get('name') + "\"" )
        rows = cur.fetchall();  
        msg = "Record successfully added"
        rowslen=len(rows)
        if rowslen<1 :
            con.rollback()
            msg = "There is no data for selected university or there is a problem in readig Data"
            return render_template("undercounst.html",rows = rows, msg = msg) 
        else:
            return render_template("transfer.html",rows = rows, msg = msg) 
            con.close();

@transferProject.route('/fourth')          # Switched to @bp.route() from @transferProject.route() <- Switched back
def fourth():
        con = sql.connect('schools.db')
        print ("Opened database successfully")
        cur = con.cursor()
        parameter=""
        firstschool=request.args.get('schoollist1')
        secondschool=request.args.get('schoollist2')
        thirdschool=request.args.get('schoollist3')
        if firstschool :
            parameter=firstschool
        if secondschool :
            parameter=parameter+","+secondschool
        if thirdschool :
            parameter=parameter+","+thirdschool
            
            
       # myquery="select * from alluniversityinfo where ID in("+firstschool+","+secondschool+","+thirdschool+") order by college "
        #myquery="select * from alluniversityinfo where ID in("+parameter+") order by INSTNM "
        #myquery="select * REPLACE(,'NULL','NOT KNOWN By Dawn') from alluniversityinfo where ID in("+parameter+") order by INSTNM "
        myquery="select ID, RANK, INSTNM, CITY, STABBR, INSTURL, transfercoursesurl, maintransferadmissionpage, employers, CONTROL, REPLACE(ADM_RATE, 'NULL', 'n/a'), REPLACE(SATVRMID, 'NULL', 'n/a'), REPLACE(SATMTMID, 'NULL', 'n/a'), REPLACE(SATWRMID, 'NULL', 'n/a'), REPLACE(ACTENMID, 'NULL', 'n/a'), REPLACE(ACTMTMID, 'NULL', 'n/a'), REPLACE(ACTWRMID, 'NULL', 'n/a'), REPLACE(CIP11BACHL, 'NULL', 'n/a'), REPLACE(UGDS, 'NULL', 'n/a'), REPLACE(UGDS_NRA, 'NULL', 'n/a'), REPLACE(COSTT4_A, 'NULL', 'n/a'), REPLACE(COSTT4_P, 'NULL', 'n/a'), UGDS_MEN, UGDS_WOMEN,REPLACE(OPEFLAG, 'NULL', 'n/a') from alluniversityinfo where ID in("+parameter+") order by INSTNM"
        #REPLACE(Null, Null, "NOT KNOWN by Dawn")

        cur.execute(myquery)
        rows = cur.fetchall();  
        msg = "Record successfully added"
        rowslen=len(rows)
        if rowslen<1 :
            con.rollback()
            msg = "There is no data for selected university or there is a problem in readig Data"
            return render_template("undercounst.html",rows = rows, msg = msg, numberofschool = rowslen) 
        else:
            msg=myquery
            return render_template("compareSchools.html",rows = rows, msg = msg, numberofschool = rowslen) 
            con.close();
    
    
   
@transferProject.route('/about')          # Switched to @bp.route() from @transferProject.route() <- Switched back
def about():
    return render_template('about.html');

@transferProject.route('/contact')          # Switched to @bp.route() from @transferProject.route() <- Switched back
def contact():
    return render_template('contact.html');


if __name__ == "__main__":
    transferProject.run(debug=True)     # Switched to @bp.route() from @transferProject.route() <- Switched back


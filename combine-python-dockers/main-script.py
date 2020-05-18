from flask import Flask,flash, render_template, request, redirect
from werkzeug.utils import secure_filename
import sys
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
import testing as fl

os.environ["TZ"] = "America/New_York"
time.tzset()

app = Flask(__name__)
app.secret_key = 'secret key'

print("CAN YOU SEE THIS")

sched = BackgroundScheduler(daemon=True)

@app.route('/')
def main():
    #datastore_client = datastore.Client()
    print('Entered main')
    return render_template('input.html')

@app.route('/forminfo',methods=['POST'])
def forminfo():
    print('Going to test now')
    def test():
        print('IN test function now')
        test = fl.mer(email1,password1,title1,description1,hashtags2,weight2)
        return test
    email1 = request.form['email']
    password1 = request.form['password']
    title1 = request.form['title']
    description1 = request.form['description']
    hashtags2 = request.form['hashtags']
    weight2 = request.form['weight']
    often2 = request.form['often']
    often2 = int(often2)
    print('Email:',email1,'Password:',password1)
    #sched = BackgroundScheduler(daemon=True)
    sched.add_job(test, 'interval', minutes=often2)
    sched.start()
    return render_template('running.html')


@app.route('/running',methods=['POST'])
def running():
    quit = request.form['quit']
    if quit == 'Yes':
        #shutil.rmtree(dirpath)
        #os.mkdir(dirpath)
        print("You've quit the program")
        sched.shutdown()
        return sys.exit()
    elif SystemExit == True:
        #shutil.rmtree(dirpath)
        #os.mkdir(dirpath)
        return sys.exit()


if __name__ == "__main__":
    #app.run(debug=True,port=int("4500"))
    #app.run(debug=True,host="0.0.0.0",port=int("4500"))
    app.run(host="0.0.0.0",port=int("4500"))
    #app.run()

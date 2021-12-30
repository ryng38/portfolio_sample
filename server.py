from flask import Flask, render_template, url_for, request, redirect   # render_template import sends the html filetype
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

#@app.route("/about.html")
#def about():
#    return render_template('about.html')
# use $env:FLASK_APP = "THE FILE NAME" THEN $FLASK_ENV='development' then flask run to open the server
@app.route("/<string:page_name>")    # can go to multiple route  w/out making individual functions
def html_page(page_name):
    return render_template(page_name)

# rather than this code below, can be done same as above
#@app.route("/works.html")
#def work():
#    return render_template('works.html')

#@app.route("/contact.html")
#def contact():
#    return render_template('contact.html')

#def write_to_file(data):     # function to save the data in contact me to a file
#    with open('database.txt', mode='a') as database:
#        email = data["email"]
#        subject = data["subject"]
#        message = data["message"]
#        file = database.write(f'EMAIL, SUBJECT, MESSAGE\n{email},{subject},{message}')

# if needed to make a csv file
def write_to_csv(data):     # function to save the data in contact me to csv file
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# the code below is for getting request
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        return 'Something went wrong, try again!'




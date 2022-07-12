
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.emails import Emails

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    emails = Emails.view_all_emails()
    return render_template('success.html', all_emails = emails)




#invisible route
@app.route('/validate', methods=['POST'])
def validate():
    session['email'] = request.form['email']
    data = {
        'email': request.form['email']
    }
    #pass data through so the function gets the whole dictionary, do not have key in, pass whole dictionary
    if not Emails.email_validation_regex(data):
        return redirect('/')
    Emails.save(data)
    return redirect('/success')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    Emails.delete(data)
    return redirect('/success')
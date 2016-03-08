#This is the controller where we handle all the moving pieces
import os
from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators
from compute import compute

app = Flask(__name__)

# This is the model
class InputForm(Form):
  something = StringField(u'Enter a website', [validators.required(), validators.length(max=50)])

# Generate a secret random key for the session
app.secret_key = os.urandom(24)

# View
@app.route('/scrapelinks/', methods=['GET', 'POST'])
def index():
  form = InputForm(request.form)
  if request.method == 'POST' and form.validate():
    something = form.something.data
    s = compute(something)
    return render_template("view_output.html", form=form, s=s)
  else:
    return render_template("view_input.html", form=form)
@app.route('/')
def homepage():
    pageType = 'home'
    title = " Title "
    paragraph = ["This site is currently under construction.", "Please pardon the mess.", "I'm still learning how to build this."]
    pageType = 'home'
    return render_template("index.html", title = title, paragraph = paragraph, pageType=pageType)
@app.route('/about/')
def aboutpage():
    title = "About"
    paragraph = ["Insert name", "probably an email", "Phone number?"]
    pageType = 'about'
    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)
@app.route('/chart/')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    something = "Making Charts"
    pageType= 'chart'
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Us', "data": [1,3,7]}, {"name": 'Them', "data": [7, 5, 2]}]
    title = {"text": 'Data Visualization'}
    xAxis = {"categories": ['2013', '2014', '2015']}
    yAxis = {"title": {"text": 'Number of Wins'}}
    return render_template('index.html', pageType=pageType, something=something, chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/test/')
def testpage():
    pageType = 'home'
    title = "Clever Title Pending"
    paragraph = ["This site is currently under construction.", "Please pardon the mess.", "I'm still learning how to build this."]
    pageType = 'home'
    return render_template("head.html", title = title, paragraph = paragraph, pageType=pageType)
@app.route('/dashboard/')
def dashboard (chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    something = "Making Charts"
    pageType= 'chart'
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Us', "data": [1,3,7]}, {"name": 'Them', "data": [7, 5, 2]}]
    title = {"text": 'Data Visualization'}
    xAxis = {"categories": ['2013', '2014', '2015']}
    yAxis = {"title": {"text": 'Number of Wins'}}
    return render_template('dashboard.html', pageType=pageType, something=something, chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


if __name__ == '__main__':
  app.run(debug = True)

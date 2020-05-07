from flask import Flask, render_template, request
app = Flask(__name__)
import json
import urllib.request

@app.route('/state')
def student():
   return render_template('state.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['nm']
      url = 'https://api.covid19india.org/v2/state_district_wise.json'
      data = urllib.request.urlopen(url).read().decode()
      obj = json.loads(data)
      for i in range(0,len(obj)):
          if(obj[i]['state'] == result):
              print(len(obj[i]['districtData']))
              return render_template("result.html",result = obj[i], length = len(obj[i]['districtData']))

if __name__ == '__main__':
   app.run(debug = True,port=8080)
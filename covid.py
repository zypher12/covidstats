from flask import Flask, render_template, request
app = Flask(__name__)
import json
import urllib.request

url = 'https://api.covid19india.org/v2/state_district_wise.json'
data = urllib.request.urlopen(url).read().decode()
obj = json.loads(data)

@app.route('/state')
def student():
   return render_template('state.html', state = obj , length = len(obj))

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['nm']
      sum = 0
      for i in range(0,len(obj)):
          if(obj[i]['state'] == result):
                for j in range(0,len(obj[i]['districtData'])):
                    sum += obj[i]['districtData'][j]['confirmed']
                return render_template("result.html",result = obj[i], length = len(obj[i]['districtData']), total = sum)

if __name__ == '__main__':
   app.run(debug = True,port=8080)
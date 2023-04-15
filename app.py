from flask import Flask, jsonify, request,render_template
import pandas as pd
from connectDB import  DB 

app = Flask(__name__, template_folder='templatesApp')
data = []

@app.route('/')
def home(): 
    con = DB()
    # df = pd.DataFrame(con.getData())
    # print("Df = ",df)
    return render_template('index.html',data = con.getData())

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    
    con = DB()
    if request.method == 'GET': 
        return jsonify(data)
    
    elif request.method == 'POST':
        content = request.get_json()
        con.insert(content)
        # data.append(content)  
        # data[0] = content
        return jsonify(content)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='192.168.1.106', port=5000)




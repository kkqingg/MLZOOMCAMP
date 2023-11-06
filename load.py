"""# ***LOAD THE FILE***"""

import pickle
from flask import Flask
from flask import request
from flask import jsonify # change back to json 

input_file = 'model_C = logisticmodel.bin'

with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('survive')

@app.route('/predict', methods=['POST'])
def predict(): # need to infrom that we're gonna get json info ,dv,model customer,dv,model
    person = request.get_json()  # chagne the json to python dictionary

    person= dv.transform([person])
    pred = model.predict_proba(person)[0,1]
    survive = pred>= 0.5              # return 0 or 1 value depending on the 0.5 

    result = {
        'survive_probability':float(pred),
        'survive':bool(survive)
    }
    return jsonify(result) 

if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0', port=9696)

#print('input', [customer])
#print('churn propabality',pred)


# THe input file is in .json format which is equal to python dictionary\
# Instead of ' ' : " " is used 


# decortor is a way to add extra functionality to our funcitons and this 
#extra functionality will turn this funciton into web service
# route will allow which address this function will leave

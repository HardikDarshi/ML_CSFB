from flask import Flask, render_template, request, make_response, send_file
import pandas as pd
import pickle
import os

import Preprocessing

app = Flask(__name__)

@app.route('/')
#def home():
#    return render_template('index.html')

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':

        Object = request.form["object"]
        if Object == 'MODRED':
            try:
                print('Entering into MODRED preocess')
                f = request.files['file1']
                df = pd.read_excel(f)
                df.columns = df.columns.str.replace(' ', '')
                columns = ['id', 'MRBTS','MODPR','redirGeranArfcnStructL','Item-redirGeranArfcnStructL-redirGeranArfcnPrio', 'Item-redirGeranArfcnStructL-redirGeranArfcnValue','redirFreqCdma','redirFreqUtraTDDL','redirGeranBandIndicator']
                preprocessor = Preprocessing.Preprocessor()

                df = preprocessor.handle_missing_values(df)
                df = preprocessor.remove_columns(df,columns)
                filename1 = 'DTmodel_Pred_MODREDV5.sav'
                loaded_model = pickle.load(open(filename1, 'rb'))
                print('MODREDV4 model loaded')
                prediction = loaded_model.predict(df)
                result = pd.DataFrame(prediction)
                result.columns = ['Pred']
                result = preprocessor.int_to_categorical(result)
                final_sheet = pd.merge(df, result, left_index = True, right_index = True)
                print('MODRED_final sheet is prepared')
                resp = make_response(final_sheet.to_csv())
                resp.headers["Content-Disposition"] = "attachment; filename=MODRED_Audit.csv"
                resp.headers["Content-Type"] = "text/csv"
                print('Please check Download folder for MODRED AUDIT Remarks sheet')
                return resp
            except Exception as e:
                print('The Exception  message is:', e)
                return 'Something is Wrong in MODRED Part'
        elif Object == 'MORED':
            try:
                print('Entering into MORED preocess')
                f = request.files['file1']
                df = pd.read_excel(f)
                df.columns = df.columns.str.replace(' ', '')
                columns = ['id', 'MRBTS','redirGeranArfcnStructL','Item-redirGeranArfcnStructL-redirGeranArfcnPrio', 'Item-redirGeranArfcnStructL-redirGeranArfcnValue','redirFreqUtraTDDL','MOPR','redirGeranBandIndicator']
                preprocessor = Preprocessing.Preprocessor()

                df = preprocessor.handle_missing_values(df)
                df = preprocessor.remove_columns(df,columns)
                filename1 = 'DTmodel_Pred_MOREDV6.sav'
                loaded_model = pickle.load(open(filename1, 'rb'))
                print('MOREDV5 model loaded')
                prediction = loaded_model.predict(df)
                result = pd.DataFrame(prediction)
                result.columns = ['Pred']
                result = preprocessor.int_to_categorical(result)
                final_sheet = pd.merge(df, result, left_index = True, right_index = True)
                print('MORED_final sheet is prepared')
                resp = make_response(final_sheet.to_csv())
                resp.headers["Content-Disposition"] = "attachment; filename=MORED_Audit.csv"
                resp.headers["Content-Type"] = "text/csv"
                print('Please check Download folder for MORED Audit Remarks sheet')
                return resp
            except Exception as e:
                print('The Exception  message is:', e)
                return 'Something is Wrong in MORED Part'

        else:
            try:
                print('Entering into REDRT preocess')
                f = request.files['file1']
                df = pd.read_excel(f)
                df.columns = df.columns.str.replace(' ', '')
                columns = ['id', 'MRBTS',"redirFreqCdma", "Item-redirGeranArfcnStructL-redirGeranArfcnPrio", 'redirGeranArfcnStructL', 'redirGeranBandIndicator','Item-redirGeranArfcnStructL-redirGeranArfcnValue']
                preprocessor = Preprocessing.Preprocessor()

                df = preprocessor.handle_missing_values(df)
                df = preprocessor.remove_columns(df,columns)
                filename1 = 'DTmodel_Pred_REDRTV1.sav'
                loaded_model = pickle.load(open(filename1, 'rb'))
                prediction = loaded_model.predict(df)
                result = pd.DataFrame(prediction)
                result.columns = ['Pred']
                result = preprocessor.int_to_categorical(result)
                final_sheet = pd.merge(df, result, left_index = True, right_index = True)
                print('REDRT_final sheet is prepared')
                resp = make_response(final_sheet.to_csv())
                resp.headers["Content-Disposition"] = "attachment; filename=REDRT_Audit.csv"
                resp.headers["Content-Type"] = "text/csv"
                print('Please check Download folder for REDRT Audit Remarks sheet')
                return resp
            except Exception as e:
                print('The Exception  message is:', e)
                return 'Something is Wrong in MORED Part'


    else:
        return render_template('index.html')

@app.route('/REDRT')
def download_REDRT():
    p= 'reference_file_REDRT.xlsx'
    return send_file(p, as_attachment= True)
@app.route('/MODRED')
def download_MODRED():
    q = 'reference_file_MODRED.xlsx'
    return send_file(q, as_attachment= True)
@app.route('/MORED')
def download_MORED():
    r = 'reference_file_MORED.xlsx'
    return send_file(r, as_attachment= True)


if __name__ == '__main__':
    #app.run(debug = True)
    #app.run(host='127.0.0.1', port=5001, debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True)

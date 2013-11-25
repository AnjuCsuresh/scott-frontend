from pymongo import MongoClient
from flask import Flask,render_template

app = Flask(__name__)
connection = MongoClient()
db = connection.google_result_extraction


def get_allresults():
	allresults = []
	for allresult in db.allresults.find():
		allresults.append(allresult)
	return allresults
def get_optmresults():
	optmresults = []
	for optmresult in db.optimized_site_list.find():
		optmresults.append(optmresult)
	return optmresults
def get_nonresults():
	nonresults = []
	for nonresult in db.non_optimized_site_list.find():
		nonresults.append(nonresult)
	return nonresults

@app.route('/')
def key():
    return render_template('key.html')
@app.route('/all')
def all_table():
	data=get_allresults()
	return render_template('table_all.html',results=data)
@app.route('/optimized')
def optm_table():
	data=get_optmresults()
	return render_template('table_optm.html',results=data)
@app.route('/nonoptimized')
def nonoptm_table():
	data=get_nonresults()
	return render_template('table_non.html',results=data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
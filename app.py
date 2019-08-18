from flask import Flask, render_template
import returncsv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
	data = pd.read_csv(returncsv.csvPath())
	head = data.head(10) #irá aparecer no html apenas as 10 primeiras linhas
	return render_template('index.html', tables=[head.to_html(classes=["table table-striped table-dark"])], titles=['Pandas com HTML'])

if __name__=='__main__':
	app.run(debug=True, port=8080)
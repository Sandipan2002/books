from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

@app.route('/', methods=["get","post"])
def index():
	if request.method == "POST":
		bookname = request.form.get("bookname")
		myurl = f"http://libgen.is/search.php?req={bookname}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
		req_obj = requests.get(myurl)
		soupObj = BeautifulSoup(req_obj.text,"lxml")
		tables = soupObj.select('table')
		data_table = tables[2]
		data = str(data_table)
	else:
		data = ""
	return render_template('index.html',data=data)


if __name__ == '__main__':
	app.run(debug = True)

from flask import Flask 

app=Flask(__name__) //object oluştur

@app.route('/') //route URL ile ilişkili.URL isteği geldiği zaman hello world fonksiyonunu çağır

def hello_world():
	return 'Hello World !\n'

if __name__ = '__main__':
	app.run(debug=True,host='0.0.0.0')

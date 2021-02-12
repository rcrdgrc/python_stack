from flask import Flask

app = Flask(__name__)

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<times>/<name>')
def repeat_name(times ,name):
    return name * int(times)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 

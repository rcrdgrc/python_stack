from flask import Flask, render_template

app = Flask(__name__)
    
@app.route('/', defaults={'y': 8, 'x': 8}) 
@app.route('/<x>', defaults={'y': 8}) 
@app.route('/<y>/<x>')
def hello_world(y, x):
    return render_template('index.html', y=int(y), x=int(x))

if __name__=="__main__":
    app.run(debug=True) 
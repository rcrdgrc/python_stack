from flask import Flask, render_template

app = Flask(__name__)
    
@app.route('/play', defaults={'times': 3, 'color': 'blue'}) 
@app.route('/play/<times>', defaults={'times': 3, 'color': 'blue'}) 
@app.route('/play/<times>/<color>')
def hello_world(times, color):
    return render_template('index.html', times=int(times), color=color)

if __name__=="__main__":
    app.run(debug=True) 
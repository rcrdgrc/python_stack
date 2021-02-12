from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/', defaults={'name': 'Name Goes Here', 'times': 5}) 
@app.route('/<name>', defaults={'times': 5}) 
@app.route('/<name>/<times>')          # The "@" decorator associates this route with the function immediately following
def hello_world(name, times):
    return render_template('index.html', name=name, times=int(times))   # Return the string 'Hello World!' as a response


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

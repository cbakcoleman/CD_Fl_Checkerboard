from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by():
    return render_template("index.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
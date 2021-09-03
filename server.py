from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by():
    return render_template("index.html")

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def sensei(num1, num2, color1, color2):
    return render_template("index.html", 
    num1 = num1, num2 = num2, 
    color1 = color1, color2 = color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
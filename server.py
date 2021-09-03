from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerbaord():
    return render_template("index.html",
    num1 = 8, num2 = 8,
    color1 = "papayawhip", color2 = "cadetblue")

@app.route('/<int:num1>')
def single(num1):
    return render_template("index.html",
    num1 = num1, num2 = 8,
    color1 = "papayawhip", color2 = "cadetblue")

@app.route('/<int:num1>/<int:num2>')
def ninja(num1, num2):
    return render_template("index.html",
    num1 = num1, num2 = num2,
    color1 = "papayawhip", color2 = "cadetblue")

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def sensei(num1, num2, color1, color2):
    return render_template("index.html", 
    num1 = num1, num2 = num2, 
    color1 = color1, color2 = color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
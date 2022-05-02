from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template('cb3.html', x=8, y=8)

@app.route('/<int:x>')
def play2(x):
    return render_template('cb3.html', x=x , y = 8)

@app.route('/<int:x>/<int:y>')
def play3(x,y):
    return render_template('cb3.html', x=x , y=y)

@app.route('/<int:x>/<int:y>/<color>')
def level3(x, y, color):
    return render_template('level3.html', x=x, y,y, color=color)
    
if __name__=="__main__": 
    app.run(debug=True)
from flask import Flask, render_template,redirect, url_for, request

def steam_valid_url(url):
    if url[0:27] == "https://steamcommunity.com/":
        return True
    else: 
        return False

    
app = Flask(__name__)

@app.route('/')
def display_main_page():
    return render_template('index.html')

@app.route('/e')
def error():
   return render_template('<p1>Scam<p1>')

@app.route('/lc',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      url = request.form['']
      if steam_valid_url:
          return redirect(url_for(''))
      else:
        return redirect(url_for('error'))
   else:
      return redirect(url_for('error'))
    

if __name__ == "__main__":
    app.run(debug=True)





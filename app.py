from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_links():
    conn = sqlite3.connect('database/smartlinks.db')  
    cursor = conn.cursor()
    cursor.execute('SELECT name, url, icon FROM links')  
    links = cursor.fetchall() 
    conn.close()  
    return links

#@app.route('/')
#def home():
    #return render_template('index.html')  

@app.route('/')
def links():
    user_links = get_links() 
    return render_template('links.html', links=user_links)   

@app.route('/add-link', methods=['GET'])
def add_link():
    name = request.args.get('name')  
    url = request.args.get('url')    
    
    if name and url:
        conn = sqlite3.connect('database/smartlinks.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO links (name, url) VALUES (?, ?)", (name, url))
        conn.commit()
        conn.close()
        return f"Le lien '{name}' a été ajouté avec succès !"
    else:
        return "Paramètres 'name' et 'url' manquants", 400

if __name__ == "__main__":
    app.run() 

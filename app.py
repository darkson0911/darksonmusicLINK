from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Fonction pour récupérer les liens
def get_links():
    conn = sqlite3.connect('database/smartlinks.db')  
    cursor = conn.cursor()
    # Inclure l'ID du lien dans la requête
    cursor.execute('SELECT id, name, url, icon FROM links')  
    links = cursor.fetchall() 
    conn.close()  
    return links

# Route pour afficher les liens
@app.route('/')
def links():
    user_links = get_links() 
    return render_template('links.html', links=user_links)   

# Route pour enregistrer les clics et rediriger
@app.route('/click/<int:link_id>')
def register_click(link_id):
    conn = sqlite3.connect('database/smartlinks.db')
    cursor = conn.cursor()
    # Incrémenter le compteur de clics
    cursor.execute("UPDATE links SET clicks = clicks + 1 WHERE id = ?", (link_id,))
    conn.commit()
    # Récupérer l'URL cible
    cursor.execute("SELECT url FROM links WHERE id = ?", (link_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return redirect(result[0])  # Redirection vers l'URL cible
    else:
        return "Lien non trouvé", 404

# Route pour ajouter un lien
@app.route('/add-link', methods=['GET'])
def add_link():
    name = request.args.get('name')  
    url = request.args.get('url')    
    
    if name and url:
        conn = sqlite3.connect('database/smartlinks.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO links (name, url, clicks) VALUES (?, ?, 0)", (name, url))
        conn.commit()
        conn.close()
        return f"Le lien '{name}' a été ajouté avec succès !"
    else:
        return "Paramètres 'name' et 'url' manquants", 400

if __name__ == "__main__":
    app.run() 

#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
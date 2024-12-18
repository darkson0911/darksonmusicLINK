import sqlite3

def init_db():
    # Connexion à la base de données (fichier physique dans database/smartlinks.db)
    conn = sqlite3.connect('database/smartlinks.db')
    cursor = conn.cursor()

    # Crée la table "links" si elle n'existe pas déjà
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL
        )
    ''')

    conn.commit()  # Sauvegarde les changements
    conn.close()   # Ferme la connexion

# Initialiser la base à l'exécution de ce fichier
if __name__ == "__main__":
    init_db()
    print("Base de données initialisée.")

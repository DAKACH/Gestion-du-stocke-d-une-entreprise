import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS Produits(
            ID Integer Primary Key,
            Nom text,
            Quantite Integer,
            Prix text,
            Date text,
            Categorie text,
            Commentaire text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, nom, quantite, prix, date, categorie, commentaire):
        self.cur.execute(
            "INSERT INTO Produits VALUES (NULL,?,?,?,?,?,?)",
            (nom, quantite, prix, date, categorie, commentaire),
        )
        self.con.commit()
        return True

    def fetch(self):
        self.cur.execute("SELECT * FROM Produits")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        try:
            self.cur.execute("DELETE FROM Produits WHERE ID=?", (id,))
            self.con.commit()
            return True, "Produit supprimé avec succès."
        except Exception as e:
            return (
                False,
                f"Erreur lors de la suppression: {str(e)}",
            )

    def is_empty(self):
        self.cur.execute("SELECT COUNT(*) FROM Produits")
        count = self.cur.fetchone()[0]
        return count == 0

    def clear(self):
        self.cur.execute("DELETE FROM Produits")
        self.con.commit()

    def update(self, id, nom, quantite, prix, date, categorie, commentaire):
        self.cur.execute(
            "UPDATE Produits SET Nom=?, Quantite=?, Prix=?, Date=?, Categorie=?, Commentaire=? WHERE ID=?",
            (nom, quantite, prix, date, categorie, commentaire, id),
        )
        self.con.commit()

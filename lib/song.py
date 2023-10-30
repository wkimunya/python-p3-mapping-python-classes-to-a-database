from config import CONN, CURSOR

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

        # After executing the insert, get the last inserted row's ID
        CURSOR.execute("SELECT last_insert_rowid() FROM songs")
        self.id = CURSOR.fetchone()[0]

        # Commit the transaction
        CONN.commit()

        return self.id

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

import sqlite3


connection = sqlite3.connect('Profile.db')
cursor = connection.cursor()

result = cursor.execute("select name from sqlite_master where type='table' and name='Cookie_Profile';").fetchone()


if not result:
    connection.execute("""
        CREATE TABLE Cookie_Profile (
            id integer primary key not null,
            created_at TEXT not null,
            cookie_value TEXT,
            last_launch TEXT,
            total_launch integer
            )
    """)

    for i in range(1, 16):
        connection.execute("""
            insert into Cookie_Profile (id, created_at, total_launch)
            values (?, datetime('now'), 0)
        """, (i,))
    connection.commit()

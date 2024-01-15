import sqlite3

latter = input()


def place():
    con = sqlite3.connect('native.db')
    cur = con.cursor()
    result = []
    for i in latter:
        res = (cur.execute("""SELECT place FROM Places
            WHERE location LIKE ?""", (i,)).fetchall())
        for j in res:
            s = cur.execute("""SELECT how_far FROM Places
                WHERE place = ?""", (''.join(j),)).fetchone()
            result.append((s, j))
    return sorted(result, reverse=True)


for i in range(len(place())):
    print(''.join(place()[i][1]))

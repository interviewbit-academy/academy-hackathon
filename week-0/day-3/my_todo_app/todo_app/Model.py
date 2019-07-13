import sqlite3 as sql

def select_todos(name):
        con = sql.connect("database.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT name FROM names WHERE name = ?", (name,));
        exist = cur.fetchall();
        if(len(exist) == 0):
            return None

        cur.execute("select todo from todos WHERE name = ?",(name,));
        
        rows = cur.fetchall(); 
        return rows;

def insert_todo(name, todo):
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("SELECT name FROM names WHERE name = ?", (name,));
                exist = cur.fetchall();
                if(len(exist) == 0):
                    cur.execute("INSERT INTO names (name) VALUES(?)", (name,));
                
                cur.execute("INSERT INTO todos  (name, todo) VALUES (?,?)",(name,todo))
                con.commit()
        except:
            con.rollback()
      
        finally:
            con.close();
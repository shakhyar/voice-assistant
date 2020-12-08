# Note: You can remove this code and make your own database system. For simplicity,
# I am using sqllite3. You can use your own fav DB modules too.
# The current database directory is /database
# make sure you delete the existing database before using it(memory.db)

import sqlite3

conn = sqlite3.connect("database/memory.db")
c = conn.cursor()


class MemoryUnit:
    """
                                        METADATA OF CLASS
    ---------------------------------------------------------------------------------------
    Connection pool: sqlite3 :: conn = sqlite3.connect("database/memory.db")
    ---------------------------------------------------------------------------------------
    Cursor of Database: sqlite3 :: c = conn.cursor()
    ---------------------------------------------------------------------------------------
    Total methods in class : MemoryUnit :: 3 methods, 1 initialisation method
    ---------------------------------------------------------------------------------------
    Server overdrive : Memory end :: conn.commit() ::: c.close() ::: conn.close()
    ---------------------------------------------------------------------------------------

    =======================================================================================
    # Method: create_table(self, true): if there is no table already created, create one, else pass.
    # using SQL for creating table-- CREATE TABLE IF NOT EXISTS memoryUnit(question TEXT, answer TEXT)
    # and creating 2 coloumns for question and answer whose data type is string
    #
    # Method: data_entry(self, question, answer): takes the question and answer, so that we can
    # assign question along with answer in the same row. SQL used.
    # INSERT INTO memoryUnit (question, answer) VALUES (?, ?)", (self.question, self.answer)
    =======================================================================================

    """
    def __init__(self):
        self.true = None
        self.question = None
        self.answer = None
        self.searchable = None

    def create_table(self, true):
        self.true = true
        if self.true:
            c.execute("CREATE TABLE IF NOT EXISTS memoryUnit(question TEXT, answer TEXT)")
            conn.commit()
        else:
            pass

    def data_entry(self, question, answer):
        self.question = question
        self.answer = answer
        c.execute("INSERT INTO memoryUnit (question, answer) VALUES (?, ?)", (self.question, self.answer))
        conn.commit()



    def read_all(self):
        c.execute("SELECT * FROM memoryUnit")
        for row in c.fetchall():
            print(row)


    def close(self):
    	c.close()
    	conn.close()

#MemoryUnit().create_table(True)
#MemoryUnit().data_entry("anything", "something")
#MemoryUnit().data_entry("this is test2", "test2 finished")
#MemoryUnit().data_entry("test3", "test3")
#MemoryUnit().read_all()

# NOTE: IF YOU WANT TO CLOSE THE CONNECTION WITHIN THIS FILE, UNCOMMENT BELOW LINES.
# IF YOU WANT TO CLOSE THE CONNECTION FROM OTHER FILE, IMPORT THIS FILE'S ALL CONTENT
# (from memory import *)

#c.close()
#conn.close()
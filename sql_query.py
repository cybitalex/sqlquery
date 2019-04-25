import mysql.connector as mysql
import os, sys

db = mysql.connect(
        host = "127.0.0.1",
        user = "alex",
        password = "adminpass"
        )
cursor = db.cursor()
#print(db)
def running_query():
    try:
        DB_NAME = input("Which database would you like to use? ")
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.Error as err:
        print("Database {} does not exist.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            connection.database = DB_NAME
        else:
            print(err)
    input1 = input("What? ")
    input2 = input("From? ")
    input3 = input("Would you like to add anything else (Y/N)? ")
    if input3.upper() == "Y":
        input_if_true = input("Where? ")
        query = "SELECT {} FROM {} WHERE {};".format(input1, input2, input_if_true)
    else:
        query = "SELECT {} FROM {};".format(input1, input2) 
    cursor.execute(query)
    query = cursor.fetchall()
#    for row in query:
#        print(row[0])
    def pp(cursor, data=None, rowlens=0):
            d = cursor.description
            if not d:
                print("#### NO RESULTS ###") 
            names = []
            lengths = []
            rules = []
            if not data:
                data = cursor.fetchall()
            for dd in d:    # iterate over description
                l = dd[1]
                if not l:
                    l = 12             # or default arg ...
                l = max(l, len(dd[0])) # Handle long names
                names.append(dd[0])
                lengths.append(l)
            for col in range(len(lengths)):
                if rowlens:
                    rls = [len(row[col]) for row in data if row[col]]
                    lengths[col] = max([lengths[col]]+rls)
                rules.append("-"*lengths[col])
            format = " ".join(["%%-%ss" % l for l in lengths])
            result = [format % tuple(names)]
            result.append(format % tuple(rules))
            for row in data:
                result.append(format % row)
            print("\n".join(result))
            
    pp(cursor, query)

running_query()

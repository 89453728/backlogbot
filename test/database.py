import sqlite3 as sq3

# some functions to manage database access in sqlite3
# 
# @ put_in_table(db: string, table_name: string, 
# keys: string array, values: values array (string or int)
# 
# insert row into a table
# * db: the database name file: example data.db
# * table_name: the sql table name to modify
# * keys: column names which you want to access
# * values: those values you want to write in
# 
# @ rem_from_table(db:string, table_name:string, 
# condition: string)
#
# remove row or rows from table with specific condition
# * condition: condition to remove for example: name != "khaled"
# check that condition is not empty because if it's empty,
# the function will throw an advise to you
#
# @ get_all_by_col(db:string, table_name:string, 
# condition:string,order: string)
#
# get all columns with specific condition to get some rows
# * order: if you want to get the data values with specific
# order, write the sql order, for example : order by name asc
#
# @ get_cols_by_col(db,table_name, keys,condition, order)
# 
# Get specific columns
#
# @ get_all(db,table_name)
#
# Get all the table rows
#
def put_in_table(db,table_name,keys,values):
        # @ example :
        # db = "data.db"
        # table_name = "register"
        # keys = ["name","age"]
        # values = [
        #       ["nasima",20],
        #       ["eliot",34]
        # ]
        # for r in values:
        #       put_in_table(db,table_name,keys,values)
        # @endexample
        assert(len(keys)==len(values))
        try:
                con = sq3.connect(db)
        except Exception:
                print("Error during the opening of sqlite3 conector")
                exit(-1)

        task = "INSERT INTO "+table_name+" ("
        for i in keys:
                task += "'"+str(i)+"',"
        task = task[0:len(task)-1] + ")"
        task += " VALUES ("
        for i in values:
                if type(i) is int :
                        task += str(i) + ","
                else:
                        task += "'" + str(i) + "',"
        task = task[0:len(task)-1] +")"
        cur = con.cursor()
        r = cur.execute(task)
        con.commit()
        con.close()
        return r

def rem_from_table(db,table_name,condition):
        # @example
        # db = "data.db"
        # table_name = "register"
        # condition = "name != 'yassin'"
        # rem_from_table(db,table_name,condition)
        # @endexample
        try:
                con = sq3.connect(db)
        except Exception as ex:
                print("Error during the opening of sqlite3 conector")
                print(ex)
                exit(-1)
        
        r = ""
        if condition == "":
                print("warning: you're going to make delete withouth condition")
                print("do you want to continue? ")
                r = input("y/n: ")
                if r == "n":
                        con.close()
                        exit(-1)
        task = "DELETE FROM "+ table_name
        if condition != "":
                task += " WHERE " + condition
        cur = con.cursor()
        cur.execute(task)
        con.commit()
        con.close()

def get_all_by_col(db,table_name,condition,order=""):
        # @example
        # db = "data.db"
        # table_name = "register"
        # condition = "name != 'yassin'"
        # order = " order by name asc"
        # d = get_all_by_col(db,table_name,condition,order)
        # print(d)
        # >> [('nadia',19),('karim',29)]
        # @endexample
        try:
                con = sq3.connect(db)
        except Exception:
                print("Error during the opening of sqlite3 conector")
                exit(-1)
        
        task = "SELECT * FROM "+table_name
        if condition != "":
                task += " WHERE" + condition
        if order != "":
                task += " " + order
        cur=con.cursor()
        r = cur.execute(task).fetchall()
        con.commit()
        con.close()
        return r
def get_cols_by_col(db,table_name,keys, condition="", order=""):
        # @example
        # db = "data.db"
        # table_name = "register"
        # keys = ['age']
        # condition = "name != 'yassin'"
        # order = " order by name asc"
        # d = get_cols_by_col(db,table_name,keys,condition,order)
        # print(d)
        # >> [(19),(29)]
        # @endexample 
        try:
                con = sq3.connect(db)
        except Exception:
                print("Error during the opening of sqlite3 conector")
                exit(-1)
        
        task = "SELECT "
        
        for i in keys[0:len(keys)-1]:
                task += "" + i + ","
        task += ""+keys[len(keys)-1]+ " "

        task +=" FROM "+table_name 
        if condition != "":
                task += " WHERE " + condition
        if order != "" :
                task += " " + order 
        cur=con.cursor()
        r = cur.execute(task).fetchall()
        con.commit()
        con.close()
        return r

def get_all(db,table_name):
        # @example
        # db = "data.db"
        # table_name = "register"
        # d = get_all(db,table_name)
        # print(d)
        # >> [('yassin',22),('nadia',19),('karim',29)]
        # @endexample 
        try:
                con = sq3.connect(db)
        except Exception:
                print("Error during the opening of sqlite3 conector")
                exit(-1)
        
        task = "SELECT * FROM "+table_name
        cur=con.cursor()
        r = cur.execute(task).fetchall()
        con.commit()
        con.close()
        return r

import database as db

keys = ["nombre","edad"]
values = [
        ["yassin",22],
        ["nadia",19],
        ["jesus",22],
        ["daniela",22],
        ["karim",29]
]



# d = db.rem_from_table("hola.db","datos","rowid > 5")
d = db.get_all("hola.db","datos")
print(d)
d = db.get_cols_by_col("hola.db","datos",["nombre","edad"],order="ORDER BY nombre ASC")
print(d)

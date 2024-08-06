from turtle import Turtle , Screen
from prettytable import PrettyTable
table=PrettyTable()
# table.field_names=["Pokemon name","Type"]
# table.add_rows(
#     [
#     ["pikachu","electric"],
#     ["squirtle","Water"],
#     ["charizard","fire"]
#     ]
# )
table.add_column("Pokemon",["piki","jhiki","liki"])
table.add_column("Type",["lichi","chichi","dichi"])
table.align="l"
print(f"{table}")

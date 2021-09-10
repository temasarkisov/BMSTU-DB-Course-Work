from __future__ import print_function
from cubes import Workspace, Cell, PointCut


workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data_sqlite/f1.sqlite")
workspace.import_model("models/model.json")

browser = workspace.browser("qualifying")


# 3. Play with aggregates
result = browser.aggregate()
print("position_min : %8d" % result.summary["position_min"])


'''
#
# 4. Drill-down through a dimension
#

print("\n"
      "Drill Down by Category (top-level Item hierarchy)\n"
      "==================================================")
#
result = browser.aggregate(drilldown=["driver_info"])
#
print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Category", "Count", "Total", "Double"))
#
for row in result.table_rows("driver_info"):
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["amount_sum"],
                              )
      )

print("\n"
      "Slice where Category = Equity\n"
      "==================================================")

cut = PointCut("item", ["e"])
cell = Cell(browser.cube, cuts = [cut])

result = browser.aggregate(cell, drilldown=["item"])

print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub-category", "Count", "Total", "Double"))

for row in result.table_rows("item"):
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["amount_sum"],
                              ))
'''
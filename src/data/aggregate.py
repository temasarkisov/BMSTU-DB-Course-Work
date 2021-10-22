from __future__ import print_function
from cubes import Workspace, Cell, PointCut


workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data_sqlite/f1.sqlite")
workspace.import_model("models/model.json")

browser = workspace.browser("qualifying")

cut1 = PointCut("drivers", [])
cut2 = PointCut("races", [])
cell = Cell(browser.cube, cuts = [cut1, cut2])
result = browser.aggregate(cell, drilldown=["drivers", "races"])

list_res = [row for row in result]

def filter_racer(data, name, year):
      temp = list(filter( 
                        lambda x: x['drivers.surname'] == name and 
                        x['races.year'] == year, 
                        data
            )
      )
      
      return sorted(temp, key=lambda x: x['position_min'])
 
for line in filter_racer(list_res, 'Hamilton', 2009): print(line)


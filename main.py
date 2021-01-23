# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import Glassdoor_scrapper as gs
import pandas as pd

path = "/Users/yuktisareen/Workspace/GitRepos/ds_salary_prj/chromedriver"

df = gs.get_jobs('data scientist', 100, False, path, 15)
df




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

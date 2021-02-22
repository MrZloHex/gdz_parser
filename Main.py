# main file
# to execute -> {dir}$python3 Main.py

import control
import DB

print("main")

DB.delete()
DB.init()
control.parse()

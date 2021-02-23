import control
import DB

# main file
# clearing and creating table
DB.delete()
DB.init()
# launching the parse process
control.parse()

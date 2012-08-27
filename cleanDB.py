
import sqlite3 as lite
import sys

print "Clean DB"
con = lite.connect('../sqlite.db')
cur = con.cursor()

f = open('.drop.cmd')
cmd_script = f.read()
cur.executescript(cmd_script)

con.commit()
con.close()

print "Done"

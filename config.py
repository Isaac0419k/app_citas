import os

MYSQLHOST = os.environ.get("MYSQLHOST", "localhost")
MYSQLPORT = int(os.environ.get("MYSQLPORT", 3306))
MYSQLUSER = os.environ.get("MYSQLUSER", "root")
MYSQLPASSWORD = os.environ.get("MYSQLPASSWORD", "")
MYSQLDATABASE = os.environ.get("MYSQLDATABASE", "votacion_app")

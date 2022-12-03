
import yfinance as yf
from datetime import date, timedelta, datetime
import time
import pymysql

#Conexión a la base de datos

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Cronopios_1",
    database = "INDICES", 
    charset = "utf8"
)

cursor = conn.cursor() 

SP500 = yf.Ticker("^GSPC") #S&P 500
Nasdaq =yf.Ticker("^NDX") #Nasdaq 100
Nasdaqcomp = yf.Ticker("^IXIC") #Nasdaq Composite
DWJ = yf.Ticker("^DJI") #Dow JOnes Industrial Average
IPC = yf.Ticker('^MXX') #IPC (BMV)
STOXX50E = yf.Ticker('^STOXX50E') #STOXX50
Nikkei = yf.Ticker('^N225') #Nikkei
CSI300 = yf.Ticker('000300.SS') #CS1300

tickets = [SP500, Nasdaq, Nasdaqcomp, DWJ, IPC, STOXX50E, Nikkei, CSI300]
ticketsname = ["SP500", "Nasdaq", "Nasdaqcomp", "DWJ", "IPC", "STOXX50", "Nikkei", "CSI300"]

#corregir


start = datetime.today().replace(hour = 0, minute = 0, second = 0 ) - timedelta(days= 1)
end = datetime.today().replace(hour = 23) - timedelta(days = 1)

        #agregar avg de open, high, low, close

"""
for i in range(len(tickets)):
    historial = tickets[i].history(start=start, end=end , interval="1m") #Obtener los tickets
    #guardamos los elementos
    filepath = Path('Info/{almacenamiento}/{name}_{date}.csv'.format(almacenamiento = ticketsname[i] ,name = ticketsname[i], date = start.strftime('%Y-%m-%d')))
    filepath.parent.mkdir(parents=True, exist_ok=True)
    #guardar gráfica
    historial.to_csv(filepath, header=True, index=True)
"""

historial = IPC.history(start = start, end = end, interval = '1m')

for row in historial:
    sql = "INSERT INTO datos(ID_INDICES, DATE_TIME, OPEN_, HIGH, LOW, CLOSE_, VOLUME, DIVIDENS, STOCK_SPLITS) VALUES(3,?,?,?,?,?,?,?,?)", (row[0].row[1],row[2],row[3],row[4],row[5],row[6],row[7])
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

conn.close()




import yfinance as yf
from pathlib import Path
from datetime import date, timedelta, datetime
import time

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

for i in range(7):
    start = datetime.today().replace(hour = 0, minute = 0, second = 0 ) - timedelta(days= i +1)
    end = datetime.today().replace(hour = 23) - timedelta(days = i +1)

        #agregar avg de open, high, low, close


    for i in range(len(tickets)):
        historial = tickets[i].history(start=start, end=end , interval="1m") #Obtener los tickets
        #Elegimos el path en el que se guardarán los csv, queremos que vaya a una carpeta adecuada a cada indicador
        filepath = Path('Info/{almacenamiento}/{name}_{date}.csv'.format(almacenamiento = ticketsname[i] ,name = ticketsname[i], date = start.strftime('%Y-%m-%d')))
        filepath.parent.mkdir(parents=True, exist_ok=True)
        #guardar gráfica
        historial.to_csv(filepath, header=True, index=True)

import yfinance as yf
from pathlib import Path
from datetime import date, timedelta, datetime
import time

SP500 = yf.Ticker("^GSPC") #S&P 500
Nasdaq =yf.Ticker("^NDX") #Nasdaq 100
Nasdaqcomp = yf.Ticker("^IXIC") #Nasdaq Composite
DWJ = yf.Ticker("^DJI") #Dow JOnes Industrial Average
IPC = yf.Ticker('^MXX') #IPC (BMV)

tickets = [SP500, Nasdaq, Nasdaqcomp, DWJ, IPC]
ticketsname = ["SP500", "Nasdaq", "Nasdaqcomp", "DWJ", "IPC"]

start = datetime.today() - timedelta(days=1)
end = datetime.today()

#agregar avg de open, high, low, close


for i in range(len(tickets)):
    historial = tickets[i].history(start=start, end=end , interval="1m") #Obtener los tickets
    #Elegimos el path en el que se guardarán los csv, queremos que vaya a una carpeta adecuada a cada indicador
    filepath = Path('Info/{almacenamiento}/{name}_{date}.csv'.format(almacenamiento = ticketsname[i] ,name = ticketsname[i], date = datetime.today().strftime('%Y-%m-%d')))
    filepath.parent.mkdir(parents=True, exist_ok=True)
    #guardar gráfica
    historial.to_csv(filepath, header=True, index=True)

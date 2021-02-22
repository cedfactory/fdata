import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

values_cac40=['AI.PA', 'AIR.PA', 'ALO.PA', 'MT', 'ATOS', 'CS.PA', 'BNP.PA', 'EN.PA', 'CAP.PA', 'CA.PA',
            'ACA.PA', 'BN.PA', 'DSY.PA', 'ENGI.PA', 'EL.PA', 'RMS.PA', 'KER.PA', 'LR.PA', 'OR.PA', 'MC.PA',
            'ML.PA', 'ORA.PA', 'RI.PA', 'PUB.PA', 'RNO.PA', 'SAF.PA', 'SGO.PA', 'SAN.PA', 'SU.PA', 'GLE.PA',
            'STLA', 'STM.PA', 'TEP.PA', 'HO.PA', 'FP.PA', 'URW.AS', 'VIE.PA', 'DG.PA', 'VIV.PA', 'WLN.PA']

def DownloadFromYahoo(values):
    for value in values:
        data_df = yf.download(value, period="max")
        filename = './data/'+value+'.csv'
        print(filename)
        data_df.to_csv(filename)

def GetDataFrameFromYahoo(value):
    result = yf.Ticker(value)
    #print(result.info)
    hist = result.history(period="max")
    return hist

def GetDataFrameFromCsv(csvfile):
    dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d')
    dataframe = pd.read_csv(csvfile,parse_dates=[0],index_col=0,skiprows=0,date_parser=dateparse)
    #df.index.rename('Time',inplace=True)
    #openValues2 = df.sort_values(by='Time')['open'].to_numpy()
    dataframe = dataframe.dropna() # remove incoherent values (null, ...)
    return dataframe


def DisplayFromDataframe(df, name):
    plt.figure(figsize=(15, 5))
    plt.plot(df[name])
    #plt.xticks(range(0, df.shape[0], 2000), df['Date'].loc[::2000], rotation=0)
    plt.ylabel(name, fontsize=18)
    plt.title(name, fontsize=20)
    plt.legend([name], fontsize='x-large', loc='best')
    plt.show()

###
### AS A SCRIPT
### python -m fdata.py
###

_usage_str = """
Options:
    [ --test, -t]
"""

def _usage():
    print(_usage_str)

def _test1():
    hist = GetDataFrameFromYahoo('AI.PA')
    print(hist)
    DisplayFromDataframe(hist, "Close")

def _test2():
    hist = GetDataFrameFromCsv('./data/AI.PA.csv')
    DisplayFromDataframe(hist, "Close")

def _download(values):
    if values == "cac40":
        DownloadFromYahoo(values_cac40)

    
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test1" or sys.argv[1] == "-t1": _test1()
        elif sys.argv[1] == "--test2" or sys.argv[1] == "-t2": _test2()
        elif sys.argv[1] == "--cac40" : _download('cac40')
        else: _usage()
    else: _usage()

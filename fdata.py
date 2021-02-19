import yfinance as yf

cac40_list=['AI.PA', 'AIR.PA', 'ALO.PA', 'MT', 'ATOS', 'CS.PA', 'BNP.PA', 'EN.PA', 'CAP.PA', 'CA.PA',
            'ACA.PA', 'BN.PA', 'DSY.PA', 'ENGI.PA', 'EL.PA', 'RMS.PA', 'KER.PA', 'LR.PA', 'OR.PA', 'MC.PA',
            'ML.PA', 'ORA.PA', 'RI.PA', 'PUB.PA', 'RNO.PA', 'SAF.PA', 'SGO.PA', 'SAN.PA', 'SU.PA', 'GLE.PA',
            'STLA', 'STM.PA', 'TEP.PA', 'HO.PA', 'FP.PA', 'URW.AS', 'VIE.PA', 'DG.PA', 'VIV.PA', 'WLN.PA']

for ticker in cac40_list:
    data_df = yf.download(ticker, period="max")
    filename = './tmp/_'+ticker+'.csv'
    print(filename)
    data_df.to_csv(filename)
    
    value = yf.Ticker(ticker)
    print(value.info)
    hist = value.history(period="max")
    print(hist['Close'])

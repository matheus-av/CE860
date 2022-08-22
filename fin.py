import yfinance as yf
import matplotlib.pyplot as plt

def ibovespa(period):
    return yf.Ticker('^BVSP').history(period = period)['Close']

def sp500(period):
    return yf.Ticker('^GSPC').history(period = period)['Close']

def dollar(period):
    return yf.Ticker('USDBRL=X').history(period = period)['Close']

def euro(period):
    return yf.Ticker('EURBRL=X').history(period = period)['Close']

def plotExchangeRates(period):
    plt.plot(dollar(period), label = 'dollar')
    plt.plot(euro(period), label = 'euro')
    plt.title("Exchange Rates") #titulo geral
    plt.xlabel("Period") #titulo eixo x
    plt.ylabel("R$") #titulo eixo y
    plt.legend() #exibe legenda passada como label no .plot()
    plt.grid() #exibe grade
    plt.show() #exibe o plot

def plotTicker(ticker):
    plt.plot(ticker)
    plt.show()

'''
uma ideia seria trazer as principais informacoes do dia
da ate pra puxar coisa de site de noticia
pegar cotacao de acoes do dia, cambio, ibovespa
um esquema tipo twitter deck
'''
import pandas
import yfinance as yf

def fetch_stock_data(ticker, period='5d', startDate=None, endDate=None):
    #print(startDate, endDate)
    if startDate == None:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
    else:
        data = yf.download(ticker, startDate, endDate)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    cost = sum(data['Close'].values) / len(data)
    print('Средняя цена закрытия: ', round(cost, 2))
    #return cost

def notify_if_strong_fluctuations(data, threshold=1):
    dif = ((max(data['Close'].values) - min(data['Close'].values)) / min(data['Close'].values)) * 100
    if dif > float(threshold):
        print(f'Колебание цены закрытия: {round(dif, 2)} %')
    else:
        print('Колебание цены закрытия в пределах указанного порога')

def export_data_to_csv(data, filename):
    data.to_csv(filename, index=False)


def calculate_rsi(data, periods=5):
    close_delta = data['Close'].diff()
    # Делаем две серии: одну для низких закрытий, другую для высоких закрытий
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    # Использование простой скользящей средней
    ma_up = up.rolling(window=periods).mean()
    ma_down = down.rolling(window=periods).mean()
    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    data['RSI'] = rsi
    return data

def calculate_standard_closing_price(data):
    df = pandas.DataFrame.std(data)
    data['STD'] = df.std()
    return data




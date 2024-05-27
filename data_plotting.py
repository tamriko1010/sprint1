import matplotlib.pyplot as plt
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(14, 8))
    print(plt.style.available)
    use_style = input('Введите стиль оформления графика из речисленных выше: ')
    plt.style.use(use_style)
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['RSI'].values, label='RSI', color='green')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['RSI'], label='RSI', color='green')
    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
    #plt.show()
    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

def create_interactive_graph(data, ticker):
    p = figure(title=f'{ticker} Цена акций с течением времени', x_axis_label='Дата', x_axis_type='datetime',
               y_axis_label='Цена', tools='reset,save')
    dates = data.index.to_numpy()
    line = p.line(dates, data['Close'].values, legend_label='Close Price', line_width=2)
    p.legend.location = 'top_left'
    hover = HoverTool()
    hover.tooltips = [('Цена', '@y')]  # Определение формата подсказки
    hover.renderers = [line]  # Применение подсказки к конкретному рендереру
    p.add_tools(hover)
    print("График сохранен как Ineractivgraf.html")
    output_file('Ineractivgraf.html')
    show(p)


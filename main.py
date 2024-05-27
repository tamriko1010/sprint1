import data_download as dd
import data_plotting as dplt

def main():
    print("Добро пожаловать в инструмент получения индикаторов теханализа акции за период времени.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    startDate = None
    endDate = None
    print('Введите стандартный период времени или конкрентные даты начала и окончания по шаблону гггг-мм-дд')
    print('Если Вам нужны конкретные даты, то стандартный период не заполняем, нажимаем "ENTER" ')
    period = input("Стандарный период (например: '1mo' для одного месяца): ")
    if period =='':
        startDate = input('Дата начала: ')
        endDate = input('Дата окончания: ')
        period = startDate + ' - ' + endDate
    threshold = input("Введите допустимый порог колебания цены акции а процентах: ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period, startDate, endDate )

    # расчет средней цены закрытия акции
    dd.calculate_and_display_average_price(stock_data)

    # Уведомление пользователя о колебании цены акции
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Экспорт данных в CSV
    dd.export_data_to_csv(stock_data, 'result.csv')

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Добавление индикатора RSI
    stock_data = dd.calculate_rsi(stock_data, periods=5)
    # расчет средней цены закрытия
    stock_data = dd.calculate_standard_closing_price(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Интерактивный график цены закрытия с всплывающей подсказкой
    dplt.create_interactive_graph(stock_data, ticker)

if __name__ == "__main__":
    main()

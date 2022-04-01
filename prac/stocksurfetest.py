from stocksurferbd import PriceData
loader = PriceData()

loader.save_history_csv(symbol='ACI', file_name='ACI_history.csv', market='DSE')
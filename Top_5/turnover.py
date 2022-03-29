# from pandas import read_html
# import bdshare

from bdshare import get_current_trade_data

df = get_current_trade_data()
print(df.to_string())

def top_turnover():
    # url = 'https://dsebd.org/dse_close_price.php'
    # dataFrame = read_html(url)
    # print(dataFrame)
    df = bdshare.get_current_trade_data()
    print(df.to_string())

top_turnover()
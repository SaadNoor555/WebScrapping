# done

from pandas import read_html
from datetime import datetime

def getPrevYearMonth():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    prevMonth = currentMonth-1 + (currentMonth==1)*12
    prevYear = currentYear
    if prevMonth == 12: prevYear-=1
    return str(prevMonth), str(prevYear)


def count_avg():
    num_of_days = [0, 31, 27, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    prevMonth, prevmonthYear = getPrevYearMonth()
    if len(prevMonth) == 1 : prevMonth = '0'+prevMonth
    end_date = prevmonthYear + '-' + prevMonth + '-' + str(num_of_days[int(prevMonth)])
    start_date = prevmonthYear + '-' + prevMonth + '-01'
    url = 'https://dsebd.org/market_summary.php?startDate='+start_date+'&endDate='+end_date+'&archive=data'
    dataFrame = read_html(url)
    print(url)
    # startDate, endDate = extractDays(url)
    # days = int(endDate[8]+endDate[9]) - int(startDate[8]+startDate[9]) + 1
    days = num_of_days[int(prevMonth)]
    tot_market_cap, tot_traded_val, tot_num_of_trades, tot_trade_vol = 0, 0, 0, 0
    
    for tab in dataFrame:
        if list(tab.columns) == [0, 1, 2, 3]:
            tot_num_of_trades += float(tab[3][1])
            tot_traded_val += float(tab[3][2])
            tot_trade_vol += float(tab[3][3])
            tot_market_cap += float(tab[3][4])

    avg_market_cap, avg_traded_val, avg_num_of_trades, avg_trade_vol = tot_market_cap/days, tot_traded_val/days, tot_num_of_trades/days, tot_trade_vol/days
    market_aggr = avg_market_cap, avg_traded_val, avg_num_of_trades, avg_trade_vol
    return market_aggr

m =count_avg() 
print(m)
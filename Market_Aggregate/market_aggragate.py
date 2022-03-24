from pandas import read_html

def extractDays(url):
    startDate , endDate = "", ""
    sflag, eflag = False, False

    for ch in url:
        if ch == '=':
            if len(startDate) == 0:
                sflag = True
            elif len(endDate) == 0:
                eflag = True
        
        elif sflag == True:
            if ch != '&':
                startDate += ch
            else:
                sflag = False
        
        elif eflag == True:
            if ch != '&':
                endDate += ch
            else:
                eflag = False
    return startDate, endDate

def count_avg():
    url = 'https://dsebd.org/market_summary.php?startDate=2022-02-01&endDate=2022-02-28&archive=data'
    dataFrame = read_html(url)

    startDate, endDate = extractDays(url)
    days = int(endDate[8]+endDate[9]) - int(startDate[8]+startDate[9]) + 1
    tot_market_cap, tot_traded_val, tot_num_of_trades, tot_trade_vol = 0, 0, 0, 0
    
    for tab in dataFrame:
        if list(tab.columns) == [0, 1, 2, 3]:
            tot_num_of_trades += float(tab[3][1])
            tot_traded_val += float(tab[3][2])
            tot_trade_vol += float(tab[3][3])
            tot_market_cap += float(tab[3][4])

    avg_market_cap, avg_traded_val, avg_num_of_trades, avg_trade_vol = tot_market_cap/days, tot_traded_val/days, tot_num_of_trades/days, tot_trade_vol/days
    return avg_market_cap, avg_traded_val, avg_num_of_trades, avg_trade_vol

print(count_avg())
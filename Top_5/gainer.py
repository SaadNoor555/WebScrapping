from bdshare import get_hist_data
from datetime import datetime

def getPrevYearMonth():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    prevMonth = currentMonth-1 + (currentMonth==1)*12
    prevYear = currentYear
    if prevMonth == 12: prevYear-=1
    return prevMonth, prevYear

def top_10_gainer():
    '''returns top 5 firms based on last month's last days turover'''
    num_of_days = [0, 31, 27, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    prevMonth, prevYear = getPrevYearMonth()
    end_date = str(prevYear) + '-' + str(prevMonth) + '-' + str(num_of_days[prevMonth])
    start_date = str(prevYear) + '-' + str(prevMonth) + '-1'

    first_day_data = get_hist_data(start_date, start_date)
    end_day_data = get_hist_data(end_date, end_date)
    # print(first_day_data)

    listOfFirms = list()
    for j in range(len(end_day_data)):
        for i in range(len(first_day_data)):
            if first_day_data.symbol[i] == end_day_data.symbol[j]:
                if float(first_day_data.value[i])!= 0:
                    '''uncomment to get top firm based on latest turnover'''
                    # cur_data = get_hist_data(end_date, end_date, first_day_data.symbol[i])
                    # turnover = (float(cur_data.ycp[j]) - float(cur_data.close[j])) / float(cur_data.close[j])
                    turnover = (float(first_day_data.ycp[i]) - float(end_day_data.close[j])) / float(end_day_data.close[j])
                    change = (float(end_day_data.value[j]) - float(first_day_data.value[i])) / float(first_day_data.value[i])
                    listOfFirms.append([first_day_data.symbol[i], turnover, change*100, float(end_day_data.value[j])])
                    break

    # print(listOfFirms)
    listOfFirms.sort(reverse = True, key = lambda x: x[1])
    top10Firms = list()
    for i in range(10):
        top10Firms.append([listOfFirms[i][0], listOfFirms[i][3], listOfFirms[i][2]])

    return top10Firms



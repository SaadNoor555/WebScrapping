from bdshare import get_hist_data

df = get_hist_data('2022-3-1', '2022-3-1') # get all instrument data
print(df.to_string())
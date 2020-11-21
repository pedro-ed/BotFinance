def index(api,par):
    profits = api.get_all_profit()
    profit = profits[par]["turbo"]*100
    return profit
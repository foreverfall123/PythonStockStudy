import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myPackage import MarketDB

mk = MarketDB.MarketDB()
stocks = ['삼성전자','SK하이닉스','현대자동차','NAVER']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2021-01-04', '2021-04-27')['close']

print(df)

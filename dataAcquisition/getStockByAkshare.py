import os
import time
import warnings
from datetime import timedelta, datetime
import akshare as ak
import pandas as pd
import numpy as np


# ##############################################打印版本号
print(f'pandas version: {pd.__version__}')
print(f'akshare version: {ak.__version__}')

############################################### 股票市场总貌
# # 股票市场总貌:上海证券交易所-股票数据总貌
# stock_sse_summary_df = ak.stock_sse_summary()
# print(stock_sse_summary_df)
#
# # 股票市场总貌:深圳证券交易所-市场总貌-证券类别统计
# stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
# print(stock_szse_summary_df)

# # 股票市场总貌:深圳证券交易所-市场总貌-地区交易排序
# stock_szse_area_summary_df = ak.stock_szse_area_summary(date="202203")
# print(stock_szse_area_summary_df)

# # 深圳证券交易所-统计资料-股票行业成交数据
# stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol="当年", date="202204")
# print(stock_szse_sector_summary_df)

# # 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况
# stock_sse_deal_daily_df = ak.stock_sse_deal_daily(date="20201111")
# print(stock_sse_deal_daily_df)

# 沪深京 A 股数据
all_stock_info = ak.stock_info_a_code_name()
print(all_stock_info)

############################################### 个股信息查询 //important
# 描述: 东方财富-个股-股票信息
# 返回代码和名称
stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
print(stock_individual_info_em_df)

############################################### 行情报价
# # 描述: 东方财富-行情报价
# stock_bid_ask_em_df = ak.stock_bid_ask_em(symbol="000001")
# print(stock_bid_ask_em_df)


############################################### 实时行情数据 //important
# 描述: 东方财富网-沪深京 A 股-实时行情数据
stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
print(stock_zh_a_spot_em_df)

# # 描述: 东方财富网-沪 A 股-实时行情数据
# stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
# print(stock_sh_a_spot_em_df)
#
# # 描述: 东方财富网-深 A 股-实时行情数据
# stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
# print(stock_sz_a_spot_em_df)
#
#
# # 描述: 东方财富网-京 A 股-实时行情数据
# stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
# print(stock_bj_a_spot_em_df)

# 描述: 东方财富网-新股-实时行情数据
stock_new_a_spot_em_df = ak.stock_new_a_spot_em()
print(stock_new_a_spot_em_df)

# # 描述: 东方财富网-创业板-实时行情
# stock_cy_a_spot_em_df = ak.stock_cy_a_spot_em()
# print(stock_cy_a_spot_em_df)
#
# # 描述: 东方财富网-科创板-实时行情
# stock_kc_a_spot_em_df = ak.stock_kc_a_spot_em()
# print(stock_kc_a_spot_em_df)
#
# # 描述: 新浪财经-沪深京 A 股数据, 重复运行本函数会被新浪暂时封 IP, 建议增加时间间隔
# stock_zh_a_spot_df = ak.stock_zh_a_spot()
# print(stock_zh_a_spot_df)
#
# # 描述: 雪球-行情中心-个股
# stock_individual_spot_xq_df = ak.stock_individual_spot_xq(symbol="SPY")
# print(stock_individual_spot_xq_df.dtypes)


############################################### 历史行情数据
# 东方财富数据：接口示例-历史行情数据-不复权
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="002466", period="daily", start_date="20170301", end_date='20240204', adjust="")
# print(stock_zh_a_hist_df.iloc[0,:])
print(stock_zh_a_hist_df.tail(1))

# # 东方财富数据：接口示例-历史行情数据-前复权
# stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="qfq")
# print(stock_zh_a_hist_df)
#
# # 东方财富数据：接口示例-历史行情数据-后复权
# stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="hfq")
# print(stock_zh_a_hist_df)

# 分时数据-东财：描述: 东方财富网-行情首页-沪深京 A 股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置

# 名称	类型	描述
# symbol	str	symbol='sh000300'; 股票代码
# start_date	str	start_date="1979-09-01 09:32:00"; 日期时间; 默认返回所有数据
# end_date	str	end_date="2222-01-01 09:32:00"; 日期时间; 默认返回所有数据
# period	str	period='5'; choice of {'1', '5', '15', '30', '60'}; 其中 1 分钟数据返回近 5 个交易日数据且不复权
# adjust	str	adjust=''; choice of {'', 'qfq', 'hfq'}; '': 不复权, 'qfq': 前复权, 'hfq': 后复权, 其中 1 分钟数据返回近 5 个交易日数据且不复权

# # 注意：该接口返回的数据只有最近一个交易日的有开盘价，其他日期开盘价为 0
# stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="000001", start_date="2021-09-01 09:32:00", end_date="2021-09-06 09:32:00", period='1', adjust='')
# print(stock_zh_a_hist_min_em_df)
#
# stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="000001", start_date="2021-09-01 09:32:00", end_date="2021-09-06 09:32:00", period='5', adjust='hfq')
# print(stock_zh_a_hist_min_em_df)

# # 日内分时数据-东财
# stock_intraday_em_df = ak.stock_intraday_em(symbol="000001")
# print(stock_intraday_em_df)
#
# # 日内分时数据-新浪
# stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sz000001", date="20231108")
# print(stock_intraday_sina_df)

# 分时数据-新浪：新浪财经-沪深京 A 股股票或者指数的分时数据，目前可以获取 1, 5, 15, 30, 60 分钟的数据频率, 可以指定是否复权

# 名称	类型	描述
# symbol	str	symbol='sh000300'; 同日频率数据接口
# period	str	period='1'; 获取 1, 5, 15, 30, 60 分钟的数据频率
# adjust	str	adjust=""; 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据;

stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol='sh600751', period='60', adjust="qfq")
print(stock_zh_a_minute_df)
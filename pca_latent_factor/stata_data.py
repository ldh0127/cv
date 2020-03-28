import pandas as pd
from pca_latent_factor.config.data import load_adj_prc


BASE_DIR = r"G:\공유 드라이브\DATA\pca_factor"

rf_path = "G:\공유 드라이브\DATA\dataguide\overall_market\eco_overnight_intermediated_transactions/eco_overnight_intermediated_transactions.csv"
rf = pd.read_csv(rf_path, parse_dates=True, index_col=0) / 100
rf.index.name = "index"
rf = ((1 + rf) ** (1 / 252)) - 1

adj_prc = load_adj_prc()
adj_return = adj_prc.diff() / adj_prc.shift(1)

rtn_rf = adj_return.sub(rf['ECO_Overnight : Intermediated Transactions(%)'], axis=0)

import glob
for i in glob.glob(f"{BASE_DIR}\*\pca.csv"):
    temp_factor = pd.read_csv(i, parse_dates=True, index_col=0)
    pd.concat([rtn_rf, temp_factor], axis=1).to_csv("\\".join(i.split("\\")[:-1]) + "\\stata.csv")



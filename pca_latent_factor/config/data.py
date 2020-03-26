import pandas as pd
from pathlib import Path

ROOT = Path(r"G:\공유 드라이브\DATA\dataguide")


def load_prc():
    close_prc_path = str(ROOT / "daily" / "close_prc" / "close_prc.csv")
    backward_adj_p = str(ROOT / "daily" / "adj_prc" / "adj_prc.csv")
    close_prc = pd.read_csv(
        close_prc_path, parse_dates=True, index_col=0, thousands=","
    )
    backward_adj_p = pd.read_csv(
        backward_adj_p, parse_dates=True, index_col=0, thousands=","
    )
    return close_prc, backward_adj_p


def load_adj_prc():
    close_prc, backward_adj_p = load_prc()
    backward_factor = backward_adj_p / close_prc
    backward_factor_init = backward_factor.bfill().iloc[0]
    forward_factor = backward_factor / backward_factor_init
    adj_prc = forward_factor * close_prc
    return adj_prc
import pandas as pd

from pathlib import Path

ROOT = Path(r"G:\공유 드라이브\DATA\dataguide")

close_prc_path = str(ROOT / "daily" / "close_prc" / "close_prc.csv")
close_prc = pd.read_csv(close_prc_path, parse_dates=True, index_col=0)

from sklearn.decomposition import PCA
PCA(n_components=5).fit_transform(close_prc[-100:].dropna(axis=1))


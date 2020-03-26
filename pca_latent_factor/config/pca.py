import sys
sys.path.append(r'C:\Users\dlehd\Desktop\git_factor\cv')

from pca_latent_factor.config.data import load_adj_prc
from sklearn.decomposition import PCA
from dateutil.relativedelta import relativedelta
from tqdm import tqdm
import pandas as pd
from datetime import datetime
from pca_latent_factor.config.config import arg_parse, make_directory, pca_path


def run(args):
    adj_prc = load_adj_prc()
    adj_return = adj_prc.diff() / adj_prc.shift(1)
    n_components = args.components
    n_years = args.years

    if args.all:
        pca_factor = agg_pca(
            adj_return,
            n_components=n_components,
            n_years=n_years
        )
        temp_pca_path = pca_path(n_components, n_years)
        temp_path = make_directory(f"{temp_pca_path}/_{datetime.today().strftime('%Y%m%d')}")
        pca_factor.to_csv(f"{temp_path}/pca.csv")
    else:
        today_factor = mypca(
            adj_return,
            datetime.today(),
            n_components=n_components,
            n_years=n_years
        )
        temp_pca_path = pca_path(n_components, n_years)
        temp_path = make_directory(f"{temp_pca_path}/{datetime.today().strftime('%Y%m%d')}")
        today_factor.to_csv(f"{temp_path}/pca.csv")


def mypca(adj_return, date, n_components, n_years):
    pca = PCA(n_components=n_components)
    temp_return = adj_return[date-relativedelta(years=n_years):date].dropna(axis=1)
    if len(temp_return.columns) <= 300:
        return None
    else:
        fit_pca = pca.fit(temp_return)
        pca_factor = (temp_return.dot(fit_pca.components_.T)).iloc[-1:]
        return pca_factor


def agg_pca(adj_return, n_components, n_years):
    pca_5_factor = []
    for date in tqdm(adj_return.index):
        temp_pca = mypca(adj_return, date, n_components, n_years)
        pca_5_factor.append(temp_pca)
    return pd.concat(pca_5_factor)


if __name__ == "__main__":
    run(arg_parse())


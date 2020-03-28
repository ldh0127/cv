import os
import itertools
import glob
import pandas as pd

BASE_DIR = r"G:\공유 드라이브\DATA\pca_factor"


def run():
    components_list = 3,5
    years_list = 1,3,5,10

    for c,y in itertools.product(components_list,years_list):
        os.system(f"python pca_latent_factor/config/pca.py --components {c} --year {y}")
    concat_pca()


def concat_pca():
    for pca_path in glob.glob(BASE_DIR + "/*"):
        pca_list = []
        for pca_csv in glob.glob(f"{pca_path}\*\pca.csv"):
            pca_list.append(pd.read_csv(pca_csv, index_col=0, parse_dates=True))
        pca_all = pd.concat(pca_list).sort_index().reset_index().drop_duplicates("index", keep="last").set_index("index")
        pca_all.to_csv(f"{pca_path}\pca.csv")


if __name__ == "__main__":
    run()
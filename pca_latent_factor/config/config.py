import argparse
from pathlib import Path
import os
BASE_DIR = Path(r"G:\공유 드라이브\DATA\pca_factor")


def pca_path(comp, year):
    return make_directory(BASE_DIR / f"{comp}_factor_{year}_year")


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        "--all",
        action="store_true"
    )
    parser.add_argument(
        "-c",
        "--components",
        default=5,
        type=int
    )
    parser.add_argument(
        "-y",
        "--years",
        default=3,
        type=int
    )
    return parser.parse_args()


def make_directory(root):
    root = root.__str__()
    if os.path.isdir(root):
        print('already_exist')
    else:
        os.mkdir(root)
    return root
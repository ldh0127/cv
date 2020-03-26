import os
import itertools

def run():
    components_list = 3,5
    years_list = 1,3,5,10

    for c,y in itertools.product(components_list,years_list):
        os.system(f"python pca_latent_factor/config/pca.py --components {c} --year {y}")

if __name__ == "__main__":
    run()

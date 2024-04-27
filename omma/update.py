import pandas as pd


def create_update_list():
    # get list of all licenses in the file
    done = pd.read_csv("table.csv")
    done_list = done['license_no'].tolist()
    # get list of all licenses in the source file
    source = pd.read_csv("source.csv")
    source_list = source['License No.'].tolist()
    # compare the two lists
    licences = list(set(source_list) - set(done_list))
    df = pd.DataFrame(licences)
    df.to_csv('update.csv', index=False)

create_update_list()
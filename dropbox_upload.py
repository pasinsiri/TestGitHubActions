import argparse
import numpy as np
import pandas as pd
import dropbox
import datetime as dt

# * retrieve dropbox credentials
parser = argparse.ArgumentParser(
    prog='DropboxAuthenticator',
    description='Get Dropbox credentials',
    epilog='The credential is required for the Dropbox connector'
)
parser.add_argument('-k', '--key')
parser.add_argument('-sc', '--secret')
parser.add_argument('-tk', '--token')
args = parser.parse_args()

# * extract credentials
key = args.key
secret = args.secret
token = args.token

# * generate random data
sample_array = np.array(
    [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    np.random.randint(low=10, high=20, size=10),
    np.random.randint(low=200, high=500, size=10)]
).T
sample_df = pd.DataFrame(sample_array, columns=['key', 'value1', 'value2'])

# * connect to dropbox and upload data
date_str = dt.datetime.strftime(dt.date.today(), '%Y-%m-%d')
dbx = dropbox.Dropbox(token)
df_io = sample_df.to_csv(index=False).encode()
dbx.files_upload(df_io, f'/Auto Uploading/sample_data_{date_str}.csv', mode=dropbox.files.WriteMode.overwrite)
print('Uploading Completed')
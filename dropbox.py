import argparse
import json

# * retrieve dropbox credentials
parser = argparse.ArgumentParser(
    prog='DropboxAuthenticator',
    description='Get Dropbox credentials',
    epilog='The credential is required for the Dropbox connector'
)
parser.add_argument('-dropbox_key', '--dropbox_key')
parser.add_argument('-dropbox_secret', '--dropbox_token')
parser.add_argument('-dropbox_token', '--dropbox_token')
args = parser.parse_args()

# * extract credentials
key = parser.dropbox_key
secret = parser.dropbox_secret
token = parser.dropbox_token

print(f'Key = {key}, Secret = {secret}, Token = {token}')
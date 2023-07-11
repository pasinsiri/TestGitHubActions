import argparse
import json

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

print(f'Key = {key}, Secret = {secret}, Token = {token}')
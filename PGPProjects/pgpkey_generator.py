import gnupg
import os

gpg = gnupg.GPG(gnupghome='/path/to/home/directory')
gpg.encoding = 'utf-8'

input_data = gpg.gen_key_input(
    name_email = '',
    passphrase = '',
    key_type = 'RSA',
    key_length = 1024
)

key = gpg.gen_key(input_data)

print(key)

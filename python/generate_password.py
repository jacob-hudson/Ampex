#!/usr/bin/env python3

import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(40)) # for a 20-character password

with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    passphrase = ' '.join(secrets.choice(words) for i in range(10))

grand_password = password + passphrase



print(grand_password.replace(' ', '_'))

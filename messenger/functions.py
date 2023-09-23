import requests
import os
import json
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64


def encryptMsg(msg):
    recipient_key = RSA.import_key(open("./public.key").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(msg.encode('utf-8'))

    return {
        'enc_session_key': base64.b64encode(enc_session_key.encode('utf-8')),
        'nonce': cipher_aes.nonce,
        'tag': tag,
        'ciphertext': base64.b64encode(ciphertext.encode('utf-8'))
    }

def decryptMsg(msg):
    private_key = RSA.import_key(open("./private.key").read())

    enc_session_key = base64.decode(msg['enc_session_key'])
    nonce = msg['nonce']
    tag = msg['tag']
    ciphertext = msg = base64.decode(msg['ciphertext'])

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    return data.decode("utf-8")

def generateKeyPair():
    key = RSA.generate(2048)
    with open("./private.key", 'wb') as content_file:
        os.chmod("./private.key", 600)
        content_file.write(key.exportKey('PEM'))
    pubkey = key.publickey()
    with open("./public.key", 'wb') as content_file:
        content_file.write(pubkey.exportKey('OpenSSH'))

def putInVault(cryptMsg):
    '''
    curl -X 'PUT'   'https://vault.immudb.io/ics/api/v1/ledger/default/collection/default/document' \
  -H 'accept: application/json' \
  -H 'X-API-Key: default.mWn4onEtvbiUi-2jD5ZdvA.tnelvIE4KpV-WJEpF46_LPrLOlCFQ5zpYwKp4s71Ox8X6WlN' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "John Doe",
    "id": 1,
    "timestamp": "2023-05-10T12:00:00Z",
    "email": "johndoe@example.com",
    "age": 30,
    "address": "123 Main Street",
    "city": "New York",
    "country": "USA",
    "phone": "+1-123-456-7890",
    "is_active": true
  }'
    '''
    headers = {
        'accept': 'application/json',
        'X-API-Key': os.getenv('VAULT_KEY'),
        'Content-Type': 'application/json'
    }
    data = {
        'msg': cryptMsg
    }
    print(data)
    req = requests.put('https://vault.immudb.io/ics/api/v1/ledger/default/collection/default/document', headers=headers, data=json.dumps(data) )

    print("Sent to vault. status code is", req.status_code )


def getLastFromVault():
    '''
    curl -X 'POST'  'https://vault.immudb.io/ics/api/v1/ledger/default/collection/default/documents/search' \
  -H 'accept: application/json' \
  -H 'X-API-Key: defaultro.idk644IhvTSUzw0pqLttPQ.LmYV3qkzc8fYQ5mK7HupIHv4NvoAw7C7YZPf_z8I2F6VUay7' \
  -H 'Content-Type: application/json' \
  -d '{"page":1,"perPage":100}'
    '''

    headers = {
        'accept': 'application/json',
        'X-API-Key': os.getenv('VAULT_KEY'),
        'Content-Type': 'application/json'
    }
    data = {"page":1,"perPage":100}
    req = requests.post('https://vault.immudb.io/ics/api/v1/ledger/default/collection/default/documents/search', headers=headers, data=json.dumps(data))

    msg = req.json()['revisions'][-1]['document']['msg']
    print("Receiving from vault:", msg)
    return msg

from functions import getLastFromVault, putInVault, generateKeyPair, encryptMsg, decryptMsg

msg = "Hey, this is pysec2023! 2"
# putInVault(msg)


# getLastFromVault()

# generateKeyPair()

msgCrypto = encryptMsg(msg)
print("cryptomsg", msgCrypto['ciphertext'])
putInVault(msgCrypto)

msgCrypto = getLastFromVault()
msg = decryptMsg(msgCrypto)
print("decrypted:", msg)

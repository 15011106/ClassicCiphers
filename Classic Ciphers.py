# Classic Ciphers created by 15011106

import random

def shift_encrypt(key,msg) :
    enc_result = ''
    for i in msg:
        enc = ord(i)-97
        a = (enc + key) % 26
        b = a + 97
        d = chr(b)
        enc_result += d

    return enc_result

def shift_decrypt(key,ctx) :
    dec_result = ''
    for i in ctx:
        dec = ord(i)-97
        a = (dec - key) % 26
        b = a + 97
        d = chr(b)
        dec_result += d

    return dec_result

def vigenere_genkey(n):
    key = []
    for i in range(n):
        c = random.randint(0,25)
        key.append(c)
    return key

def vigenere_encrypt(key,msg):
    enc_result = ''
    var = 0
    mod = len(key)
    for i in msg:
        enc = ord(i) - 97
        a = (enc+(key[var%mod])) % 26
        b = a + 97
        d = chr(b)
        enc_result += d
        var +=1
    return enc_result

def vigenere_decrypt(key,ctx):
    dec_result = ''
    var = 0
    mod = len(key)
    for i in ctx:
        dec = ord(i)-97
        a = ((dec - key[var%mod])) % 26
        b = a + 97
        d = chr(b)
        dec_result += d
        var += 1
    return dec_result

def lfsr_genkey(n):
    c = []
    x = []
    key = []
    for i in range(n):
        c.append(random.randint(0,25))
        x.append(random.randint(0,25))
        key = [c,x]
    return key

def lfsr_encrypt(key,msg):
    enc_result = ''
    var = len(key[0])
    prf = 0
    j = 0
    for i in range(len(msg)):
        j = i
        for n in range(0,var):
            prf = prf + (key[0][n]*key[1][j])
            j += 1
        gen_prf = prf%26
        key[1].append(gen_prf)
        
    for i in msg:
        enc = ord(i) - 97
        a = (enc + key[1][var]) % 26
        b = a + 97
        d = chr(b)
        enc_result += d
        var += 1
    return enc_result

def lfsr_decrypt(key,ctx):
    dec_result = ''
    var = len(key[0])
    for i in ctx:
        dec = ord(i) - 97
        a = (dec - key[1][var]) % 26
        b = a + 97
        d = chr(b)
        dec_result += d
        var += 1
    return dec_result

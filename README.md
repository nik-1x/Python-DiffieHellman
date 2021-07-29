# Python-DiffieHellman

Hi! Its test repository. Here im testing Diffie Hellman key exchange method.

## Example
```python
from DHLib import Encrypt
enc = Encrypt()

# for example we have
a: int = 1521255211
g: int = 125125
p: int = 51251080512

# now we need A: A=g^a mod p
A: int = enc.do(g, a, p)
print(A) # result: 22164961885
```


## Diffie Hellman key exchange method

> You can find more information about Diffie Hellman key exchange [here](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange).

## Links

My GitHub -- [click to go](https://github.com/nikitt-code)

My Telegram -- [click to go](https://t.me/niki_tt)

Diffie Hellman wiki page -- [click to go](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)

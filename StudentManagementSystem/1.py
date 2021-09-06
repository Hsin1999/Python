import hmac
s=hmac.new(b'hsin', 'data'.encode('utf8'), digestmod='sha256')
print(s.hexdigest())
import os
a=os.path.abspath('.')
print(a)
with open(a+r'\files\main.txt', 'r', encoding='utf8') as f:
    print(f.read())
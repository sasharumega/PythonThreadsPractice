from hashlib import md5
import time
from random import choice

counter = 0
start = time.time()

while counter < 30:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("000"):
        print(s, h)
        counter += 1
print('Time: ' + format(time.time() - start, '.1f'))
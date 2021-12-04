from hashlib import md5
import time
from concurrent.futures import ProcessPoolExecutor
from random import choice

def run_one_step():
	while True:
		s = "".join([choice("0123456789") for i in range(50)])
		h = md5(s.encode('utf8')).hexdigest()
		if h.endswith("000"):
			break
	print(s, h)
	return s, h


if __name__ == '__main__':

	start = time.time()

	with ProcessPoolExecutor(max_workers=4) as executor:
		for i in range(30):
			executor.submit(run_one_step)

	print('Time: ' + format(time.time() - start, '.3f'))

import time
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
import concurrent.futures
from urllib.parse import unquote
from tqdm import tqdm


def check_link(url):
    global counter
    counter += 1
    print('Checking: ' + format(100 * counter/len(links), '.2f') + '%  Elapsed: ' + format(time.time() - start, '.1f'))
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        resp.close()
    except Exception as e:
        pass


links = open('res.txt', encoding='utf8').read().split('\n')

counter = 0
start = time.time()
with ThreadPoolExecutor(max_workers=20) as executor:
    for _ in executor.map(check_link, links):
        pass

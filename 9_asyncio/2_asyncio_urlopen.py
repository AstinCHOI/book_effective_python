# https://dojang.io/mod/page/view.php?id=1167

from time import time
from urllib.request import Request, urlopen
import asyncio
 
urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]
 
async def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})    # UA가 없으면 403 에러 발생
    response = await loop.run_in_executor(None, urlopen, request)    # run_in_executor 사용
    page = await loop.run_in_executor(None, response.read)           # run in executor 사용
    return len(page)
 
async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
                                                           # 태스크(퓨처) 객체를 리스트로 만듦
    result = await asyncio.gather(*futures)                # 결과를 한꺼번에 가져옴
    print(result)
 
begin = time()
loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(main())          # main이 끝날 때까지 기다림
loop.close()                             # 이벤트 루프를 닫음
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))


# 만약, run_in_executor에 인자로 함수를 사용할 경우, 
# functools.partial 함수를 사용해야한다.
# import functools
# async def hello(executor):
#     await loop.run_in_executor(None, functools.partial(print, 'Hello', 'Python', end=' '))

# >>> import functools
# >>> hello = functools.partial(print, 'Hello', 'Python', end=' ')    # 'Hello', 'Python' end=' '이 
# >>> hello()                                                         # 포함된 함수 생성
# Hello Python 
# >>>hello('Script', sep='-')    # 부분 함수에 다시 'Script'와 sep='-'를 넣어서 호출
# Hello-Python-Script
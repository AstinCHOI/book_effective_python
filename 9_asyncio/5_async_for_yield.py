# 출처: https://dojang.io/mod/page/view.php?id=1167

import asyncio
 
async def async_counter(stop):    # 제네레이터 방식으로 만들기
    n = 0
    while n < stop:
        yield n
        n += 1
        await asyncio.sleep(1.0)
 
async def main():
    async for i in async_counter(3):    # for 앞에 async를 붙임
        print(i, end=' ')

 	# python 3.6
    # a = [i async for i in AsyncCounter(3)]
    # print(a)    # [0, 1, 2]
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
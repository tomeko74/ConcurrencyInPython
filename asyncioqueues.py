"""
import asyncio
import time


async def myWorker(lock):
    print("Attempting to attain lock")
    # acquire lock
    with await lock:
        # run critical section of code
        print("Currently Locked")
        time.sleep(2)
    # our worker releases lock at this poit
    print("Unlocked Critical Section")


async def main():
    # instantiate our lock
    lock = asyncio.Lock()
    # await the execution of 2 myWorker coroutines
    # each with our same lock instance passed in
    await asyncio.wait([myWorker(lock), myWorker(lock)])

# Start up a simple loop and run our main function
# until it is complete
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("All Tasks Completed")
loop.close()
"""

import asyncio
import random


async def newsProducer(myQueue):
    while True:
        await asyncio.sleep(1)
        print("Putting news item onto queue")
        await myQueue.put(random.randint(1,5))


async def newsConsumer(id, myQueue):
    print(myQueue)
    while True:
        print("Consumer: {} Attempting to get from queue".format(id))
        item = await myQueue.get()
        if item is None:
            # the producer emits None to indicate that it is done
            break
        print("Consumer: {} consumed article with id: {}".format(id, item))


async def main(loop):
    myQueue = asyncio.Queue(loop=loop, maxsize=10)
    await asyncio.wait([newsProducer(myQueue), newsConsumer(1, myQueue), newsConsumer(2, myQueue)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print("All workers completed")
loop.close()


import asyncio
# import uvloop


class AsyncLibrary(object):
    def get_future(self):
        the_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(the_loop)
        the_future = asyncio.Future()

        async_lib_result = {
            'loop': the_loop,
            'future': the_future
        }

        return async_lib_result

    def get_future_from_loop(self, the_loop):
        asyncio.set_event_loop(the_loop)
        the_future = asyncio.Future()

        return the_future

    def close_loop(self, the_loop):
        the_loop.close()

    def execute_async(self, function, the_loop, the_future):
        asyncio.ensure_future(function)
        the_loop.run_until_complete(the_future)

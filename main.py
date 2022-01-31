import asyncio

event = {
    'test_key' : 'test_value',
    'test_key_2': 'test_value_2'
}


def handler(event, context):
    asyncio.run(async_wrapper(event)) # run functions concurrently
    return None


async def send_email(*args, **kwargs):
    print('send email')
    print(*args)
    print(**kwargs)


async def send_sns(*args, **kwargs):
    print('send sns')
    print(*args)
    print(**kwargs)

async def async_wrapper(*args, **kwargs):
    await asyncio.gather(
            send_email(*args, **kwargs),
            send_sns(*args, **kwargs)
            # if you want to do more job. just add more functions in asyncio.gather's arguments.
        )


if __name__ == '__main__':
    handler(event, {})
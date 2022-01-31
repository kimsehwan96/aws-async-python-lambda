# AWS ASYNCIO PYTHON LAMBDA

## 비동기 처리 AWS LAMBDA

Python3.7 이상의 람다 런타임에서 사용 가능하다.


```python3
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
```

대부분의 경우 AWS LAMBDA는 내부 로직을 동기처리해도 큰 이슈는 발생하지 않는다. 

다만 글로벌 리전 서비스를 하는 경우, `cross-region`하게 서비스를 호출하는 경우 (예: 서울 리전에서 외국 리전의 sns 문자 전송 서비스를 사용 해야 할 경우. / 서울 리전은 sns 문자 서비스를 지원하지 않음) 동기 로직을 사용하게 되면 boto3 client 혹은 api call 을 하는 과정에서 꽤나 긴 처리시간이 들고, 다른 로직이 블로킹 된다.

이는 궁극적으로 lambda 사용 비용 증가 및 사용자 경험 저하의 원인이 된다. 

따라서 동기처리를 하지 않아도 되는 로직일 경우 유용할 패턴이다.

### 왜 다른 람다 비동기 호출은 사용하지 않나요?

다른 람다를 비동기 호출하여 동시 사용해도 된다. 하지만 다른 람다가 호출되고, 로직을 타는 과정에서 추가 비용이 발생 할 수 있기 때문에 이렇게 사용해보았다.

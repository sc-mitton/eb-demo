from celery import shared_task


@shared_task(retry_backoff=10, retry_jitter=True,
             retry_kwargs={'max_retries': 3})
def dummy_beat(*args, **kwargs) -> None:
    print('Dummy task executed')

import time
import logging
from celery import shared_task


@shared_task
def hello():
    for i in range(10):
        print("Hello World!")
        print("Hello Mazen!")
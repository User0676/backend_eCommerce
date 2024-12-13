# orders/tasks.py
from celery import shared_task
from time import sleep
import logging
logger = logging.getLogger(__name__)

@shared_task(max_retries=3)
def process_order(order_id):
    logger.info("Task started...")
    sleep(5)
    print(f'Order {order_id} processed successfully')
    return f'Order {order_id} completed'


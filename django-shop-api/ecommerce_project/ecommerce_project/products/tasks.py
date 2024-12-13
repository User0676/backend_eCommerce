# products/tasks.py
from celery import shared_task
import logging
logger = logging.getLogger(__name__)

@shared_task(max_retries=3)
def send_order_confirmation_email(order_id):
    logger.info("Task started...")
    print(f"Order confirmation email sent for order ID: {order_id}")
    return f"Email sent for order ID: {order_id}"

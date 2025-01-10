import pika
import json
import os

# RabbitMQ configuration
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
OUTPUT_QUEUE = os.getenv('OUTPUT_TOPIC', 'output_topic')

def on_message(ch, method, properties, body):
    # Deserialize the message
    message = json.loads(body)
    print(f"Received message from queue '{OUTPUT_QUEUE}': {message}")

def subscribe_to_messages():
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declare the queue to ensure it exists
    channel.queue_declare(queue=OUTPUT_QUEUE)

    # Set up a subscription to the queue
    channel.basic_consume(
        queue=OUTPUT_QUEUE,
        on_message_callback=on_message,
        auto_ack=True
    )

    print(f"Subscribed to queue '{OUTPUT_QUEUE}'. Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    subscribe_to_messages()

import pika
import json
import os

# RabbitMQ configuration
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
INPUT_QUEUE = os.getenv('INPUT_TOPIC', 'input_topic')

def publish_message():
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declare the queue to ensure it exists
    channel.queue_declare(queue=INPUT_QUEUE)

    # Example message to send
    message = {
        "example_key": "example_value"
    }

    # Publish the message to the queue
    channel.basic_publish(
        exchange='',
        routing_key=INPUT_QUEUE,
        body=json.dumps(message)
    )

    print(f"Message published to queue '{INPUT_QUEUE}': {message}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    publish_message()

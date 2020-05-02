#! /usr/bin/env python3

import pika
import json


class Subscriber:
    def __init__(self, callback, exchange_name='test',
                 routing_key="", host="localhost"):
        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self.host = host
        self.custom_callback = callback

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(
            exchange=self.exchange_name, exchange_type='topic')

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue

    def callback(self, ch, method, properties, body):
        data = json.loads(body)
        self.custom_callback(data)

    def start_consuming(self):
        self.channel.queue_bind(exchange=self.exchange_name,
                                routing_key='', queue=self.queue_name)

        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    def callback(data):
        print("retrieved data -> %r" % data)

    import sys
    exchange_name = sys.argv[1] if len(sys.argv) > 1 else 'test'

    try:
        sub = Subscriber(callback, exchange_name=exchange_name)
        sub.start_consuming()

    except(KeyboardInterrupt):
        sub.close_connection()
        print("\nClosed connection.")

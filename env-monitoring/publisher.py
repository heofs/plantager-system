#! /usr/bin/env python3

import pika
import json
import time


class Publisher:
    def __init__(self, exchange_name='test',
                 routing_key="", host="localhost"):
        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self.host = host

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange=self.exchange_name,
                                      exchange_type='topic')

    def publish_data(self, data):
        self.channel.basic_publish(exchange=self.exchange_name,
                                   routing_key=self.routing_key,
                                   body=json.dumps(data))

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    pub = Publisher()
    inc = 1
    while 1:
        pub.publish_data({"seconds": inc})
        inc += 1
        time.sleep(1)
    pub.close_connection()

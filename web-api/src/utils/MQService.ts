import amqp from 'amqplib';

const CONN_URL = process.env.RABBIT_MQ_URL || 'amqp://rabbitmq';

export const publish = async (exchangeName: string, message: any) => {
  const connect = await amqp.connect(CONN_URL);
  const channel = await connect.createChannel();

  await channel.assertExchange(exchangeName, 'topic', { durable: false });
  await channel.publish(exchangeName, '', Buffer.from(message));

  // console.log('Message published: ', exchangeName, message);
};

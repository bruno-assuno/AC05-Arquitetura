#!/usr/bin/env python
import requests
import pika

dicionarioEndereco = requests.get('https://brasilapi.com.br/api/cep/v1/03249050')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

mensagem = str(dicionarioEndereco.json())
channel.basic_publish(exchange='logs', routing_key='', body=mensagem)
print(" [x] Sent %r" % mensagem)
connection.close()
import pika
import json
import uuid

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar una cola para el procesamiento de imágenes
channel.queue_declare(queue='image_processing_queue')

def send_image_processing_request(image_path):
    # Crear un mensaje con los detalles de la imagen
    message = {
        'id': str(uuid.uuid4()),  # Un identificador único para la solicitud
        'image_path': image_path
    }

    # Publicar el mensaje en la cola
    channel.basic_publish(
        exchange='',
        routing_key='image_processing_queue',
        body=json.dumps(message)
    )
    print(f" [x] Sent image processing request for {image_path}")
    connection.close()

import random
import pika
import json


def process_image(image_path):
    # Simulación de procesamiento de imágenes
    try:

        # Realiza alguna operación de procesamiento, por ejemplo, redimensionar la imagen


        processed_image_path = f'processed_new_image{random.randint(1,1000)}.jpg'

        print(f" [x] Processed image saved as {processed_image_path}")
    except Exception as e:
        print(f" [!] Error processing image : {e}")

def callback(ch, method, properties, body):
    # Deserializar el mensaje JSON
    message = json.loads(body)
    image_path = message['image_path']
    print(f" [x] Received request to process image {image_path}")
    # Procesar la imagen
    process_image(image_path)

def start_consuming():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='image_processing_queue')

    channel.basic_consume(
        queue='image_processing_queue',
        on_message_callback=callback,
        auto_ack=True
    )

    print(' [*] Waiting for image processing requests. To exit press CTRL+C')
    channel.start_consuming()

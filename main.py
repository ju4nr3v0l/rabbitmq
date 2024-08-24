import multiprocessing
import producer
import consumer


def run_producer():
    # Enviar  imágenes
    producer.send_image_processing_request('/path/to/image1.jpg')



def run_consumer():
    consumer.start_consuming()


if __name__ == '__main__':
    # Crear un proceso para el productor
    producer_process = multiprocessing.Process(target=run_producer)

    # Crear un proceso para el consumidor
    consumer_process = multiprocessing.Process(target=run_consumer)

    # Iniciar ambos procesos
    producer_process.start()
    consumer_process.start()

    # Esperar a que ambos procesos terminen
    producer_process.join()
    consumer_process.join()

import pika, os, json, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()
from products.models import Product
from dotenv import load_dotenv
load_dotenv()
params = pika.URLParameters(os.environ.get('RABBITMQ_CONNECT_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print(" [x] Received in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes += 1
    product.save()
    print(f'{product.likes} : Number of likes of the product')


channel.basic_consume(queue='admin',on_message_callback=callback, auto_ack=True)
print(' [*] Started consuming')
channel.start_consuming()

channel.close()
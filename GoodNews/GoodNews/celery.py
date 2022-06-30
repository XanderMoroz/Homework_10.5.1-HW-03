# В первую очередь мы импортируем библиотеку для работы с операционной системой и саму библиотеку Celery.
import os
from celery import Celery
# Второй строчкой мы связываем настройки Django с настройками Celery через переменную окружения.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GoodNews.settings')
# Далее мы создаём экземпляр приложения Celery,
app = Celery('GoodNews')
# устанавливаем для него файл конфигурации. Мы также указываем пространство имён,
# чтобы Celery сам находил все необходимые настройки в общем конфигурационном файле settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Последней строчкой мы указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта.
app.autodiscover_tasks()

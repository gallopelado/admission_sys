"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()


bind = '0.0.0.0:' + environ.get('PORT', '5000')
worker_connections = 1000
max_requests = 2000
timeout = 30

loglevel = 'info'
errorlog = '-'
accesslog = '-'

reload = True
debug = False
worker_class = 'gevent'
workers = max_workers()

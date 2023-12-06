import sys

DATABASE_PATH = 'clientes.csv'
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'
    print('Running in test mode')
else:
    print('Running in production mode')
FLASK_NAME = 'FLASK_TEMPLATE' # Имя Flask (По умолчанию: __name__)

FLASK_RUN = { # Настройки запуска Flask
    'host':'127.0.0.1', # Хост веб-сервера
    'port':'5000', # Порт веб-сервера
    'debug':True, # Дебаг
    'load_dotenv':True # Загрузка .env
    # Словарь аналогичен Flask(**FLASK_RUN)
} # (По умолчанию: {})

FLASK_SECRET_KEY = None # Секретный ключ для Flask (По умолчанию: None) (str|None)

FLASK_DIRS = { # Настройки папок Flask
    'static':'static/', # Папка для static (По умолчанию: static/)
    'templates':'templates/' # Папка для templates (По умолчанию: templates/)
} # (По умолчанию: {})

FLASK_GLOBALS = { # Предзапуск функций
    'outer':[ # Внешние функции работают до обработки настроек
        'libs.globals.globals_example'
    ],
    'inner':[ # Внутренние функции работают после обработки настроек
        'libs.globals.globals_example'
    ]
} # (По умолчанию: {})


MIDDLEWARES = [ # Мидлвари для запросов
    'libs.middlewares.MiddlewareExample'
] # (По умолчанию: [])


APPS = { # Приложения с запросами
    '__dir__':None, # Каталог, в котором происходит поиск приложений, по умолчанию: в корне запуска (str|None)
    'mytest':[ # Название приложения/каталога
        'libs.middlewares.MiddlewareExample'
        # Мидлвари для приложения
    ]
} # (По умолчанию: {})


# Осторожно! Далее: Для разработчиков
VARS = {
    'router':'router', # Переменная роутера для приложений. По умолчанию: router
    'app_init':'' # Расположение файла основного файла приложения. По умолчанию: ''(Будет запуск файла __init__.py)
}  # (По умолчанию: {})
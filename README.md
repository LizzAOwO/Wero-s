# Wero´s Tacos
Proyecto de ingenieria de software
## Coneccion con mysql
 wero\settings.py

 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurante_db', -> nombre de la base de datos
        'USER': '<cambia esto>', -> usuario de acceso a mysql
        'PASSWORD': '<cambia esto>', -> contraseña del usuario
        'HOST': '127.0.0.1', -> esto es configuracion default
        'PORT': '3306',      -> esto es configuracion default
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
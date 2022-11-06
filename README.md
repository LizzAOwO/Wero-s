# Wero´s Tacos
Proyecto de ingenieria de software
### Coneccion con mysql
 -> `wero\settings.py`  
 
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'restaurante_db', -> nombre de la base de datos  
        'USER': '[nombre de usuario en msql]',  
        'PASSWORD': '[contraseña del usuario msql]',  
        'HOST': '127.0.0.1',   
        'PORT': '3306',  
        'OPTIONS':{  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}
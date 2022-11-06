# Wero´s Tacos
Proyecto de ingenieria de software
### Coneccion con mysql
 -> `wero\settings.py`  
 
DATABASES = {  
<<<<<<< HEAD
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
=======
    &emsp;'default': {  
       &emsp;&emsp; 'ENGINE': 'django.db.backends.mysql',  
       &emsp;&emsp; 'NAME': 'restaurante_db', -> nombre de la base de datos  
       &emsp;&emsp; 'USER': '[nombre de usuario en msql]',  
       &emsp;&emsp; 'PASSWORD': '[contraseña del usuario msql]',  
       &emsp;&emsp; 'HOST': '127.0.0.1',   
       &emsp;&emsp; 'PORT': '3306',  
       &emsp;&emsp; 'OPTIONS':{  
       &emsp;&emsp;&emsp;     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
       &emsp;&emsp; }  
   &emsp;}  
}
>>>>>>> e3860488ffe829ac54a3c74d00efc390b2cd4f5a

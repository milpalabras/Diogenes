# Diógenes

Diógenes es una aplicacion de finanzas personales desarrollada en Django para control y estadisticas de gastos.

<br />
> Caracteristicas

- Minimas dependencias
- Bootstrap
- UI: _HTML, CSS, JS_ 
-`SQLite Database`, Django ORM
- `Autenticación de usuarios`, Validación de formularios


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

Necesitaras tener Python instalado en tu maquina local.

_Puedes descargarlo e instalarlo con el siguiente link:_
- 👉 [Python 3.10.4](https://www.python.org/downloads/release/python-3104/) - Sitio Oficial


### Instalación 🔧

_Pasos necesarios para obtener el codigo y ejecutarlo_

_Clona el repositorio_
```
git clone https://github.com/milpalabras/Diogenes.git
```

_accede al directorio y activa el entorno virtual_
```
cd Diogenes
virtualenv env
.\env\Scripts\activate
```

_Instala los requerimientos_
```
pip3 install -r requirements.txt
```

_Crea la base de datos SQLite y las tablas_
```
python manage.py makemigrations
python manage.py migrate
```

_el repositorio cuenta con archivo de categorias ya creadas(categorias.json). Para utilizarlo ejecuta_
```
python manage.py loaddata categorias.json
```

_Inicia el servidor_
```
python manage.py runserver
```

_Accede al servidor a traves de la url http://127.0.0.1:8000/_

## Estructura del proyecto ⚙️

La estructura del proyecto esta diseñado de la siguiente manera:

```bash
< Diogenes >
   |
   |-- core/                               # Configuracion del core del sistio
   |    |-- settings.py                    
   |    |-- wsgi.py                        
   |    |-- urls.py                        
   |
   |-- apps/
   |    |
   |    |-- home/                          # App para controlar la pagina de inicio
   |    |    
   |    |-- dashboard/                     # App para graficos y variables del inicio
   |    |    
   |    |-- accounts/                      # Login, Register, Cambio de contraseña
   |    |
   |    |-- finanzas/                      # App central que controla los registros, cuentas, categorias
   |    |    
   |    |-- mensajeria/                    # App para mensajeria entre usuarios
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS,Javascripts 
   |    |
   |    |-- templates/                     # Templates para renderizar las paginas
   |         |-- includes/                 
   |         |
   |         |-- layouts/                  
   |         |
   |         |-- accounts/                 
   |         |
   |         |-- home/                     
   |         |
   |         |-- finanzas/                 
   |         |
   |         |-- mensajeria/               
   |
   |-- requirements.txt                     
   |
   |-- manage.py                            
   |
   |-- ************************************************************************
```




## Construido con 🛠️

_Herramientas utilizadas para el proyecto_

* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
* [Botstrap](https://getbootstrap.com/) - The most popular HTML, CSS, and JS library in the world.
* [Visual Studio Code](https://code.visualstudio.com/) - Code editing.Redefined.


## Autor ✒️


* **Sergio Gomez** - *Idea y creación* - [Sergio Gomez](https://github.com/milpalabras)
* **MilPalabras Estudio de diseño integral** - [MILPALABRAS](http://milpalabras.com.ar/)


## Licencia 📄

Este proyecto está bajo la Licencia MIT License - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Agradecimientos  🎁

* Franco Di Martino [FrancoDiMartino](https://github.com/FrancoDiMartino)
* CoderHouse 

---
con ❤️ por [Sergio Gomez](https://github.com/milpalabras) 😊
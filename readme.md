# Di贸genes

Di贸genes es una aplicacion de finanzas personales desarrollada en Django para control y estadisticas de gastos.
![](https://github.com/milpalabras/Diogenes/blob/master/apps/static/assets/img/Diogenes_screenshoots.png)

### [App en Heroku](https://diogenes-mvp.herokuapp.com/)

<br />
> Caracteristicas

- Minimas dependencias
- Bootstrap
- UI: _HTML, CSS, JS_ 
-`SQLite Database`, Django ORM
- `Autenticaci贸n de usuarios`, Validaci贸n de formularios


## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._


### Pre-requisitos 馃搵

Necesitaras tener Python instalado en tu maquina local.

_Puedes descargarlo e instalarlo con el siguiente link:_
- 馃憠 [Python 3.10.4](https://www.python.org/downloads/release/python-3104/) - Sitio Oficial


### Instalaci贸n 馃敡

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

_Inicia el servidor_
```
python manage.py runserver
```

_Accede al servidor a traves de la url http://127.0.0.1:8000/_

## Registros de ejemplo

_En caso de querer importar registros a la base de datos, existe una archivo .json en el repositorio con datos ficticios_
_Ejecuta el siguiente codigo para importarlos_
```
python manage.py loaddata registros_de_ejemplo.json
```

## Estructura del proyecto 鈿欙笍

La estructura del proyecto esta dise帽ado de la siguiente manera:

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
   |    |-- accounts/                      # Login, Register, Cambio de contrase帽a
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




## Construido con 馃洜锔?

_Herramientas utilizadas para el proyecto_

* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
* [Botstrap](https://getbootstrap.com/) - The most popular HTML, CSS, and JS library in the world.
* [Visual Studio Code](https://code.visualstudio.com/) - Code editing.Redefined.


## Autor 鉁掞笍


* **Sergio Gomez** - *Idea y creaci贸n* - [Sergio Gomez](https://github.com/milpalabras)
* **MilPalabras Estudio de dise帽o integral** - [MILPALABRAS](http://milpalabras.com.ar/)


## Licencia 馃搫

Este proyecto est谩 bajo la Licencia MIT License - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Agradecimientos  馃巵

* Franco Di Martino [FrancoDiMartino](https://github.com/FrancoDiMartino)
* CoderHouse 

---
con 鉂わ笍 por [Sergio Gomez](https://github.com/milpalabras) 馃槉

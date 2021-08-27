# Guía para PY1

Esta es una pequeña guía que podrán utilizar ustedes para tener su aplicación en heroku y que nosotros los auxiliares podamos acceder a ella desde nuestro navegador para la calificación. Hay que tomar en cuenta que este ejemplo lo relizamos utilizando Flask.

## Heroku

Es una plataforma de servicios en la nube, cuya popularidad ha crecido en los últimos años debido a su facilidad de uso y versatilidad para distintos proyectos.

Para usarlo se necesitará crear una cuenta, además de instalar Heroku CLI.

## Flask

Es un micro Framework escrito en Python y desarrollado para simplificar y hacer más fácil la creación de aplicaciones web bajo el patrón MVC.

Para usarlo únicamente tendrémos que instalarlo en nuestro entorno usando pip.

## Despliegue

### Prerrequisitos

- Python
- pip
- pipenv
- Heroku CLI
- Git

### Pasos

1. Crearemos un entorno virtual con pipenv y le instalamos todas las dependencias que necesitaremos. Obligatoriamente agregar flask y gunicorn.

```cmd
pipenv install flask gunicorn ...
```

2. Crearemos el archivo Procfile. Este es un archivo que especifica los comandos que se ejecutarán en la aplicación en su arranque. Dentro de este colocaremos el siguiente código

```text
web: gunicorn wsgi:app
```

3. (Opcional) Crearemos un archivo runtime.txt con el siguiente código.

```text
python-3.9.6
```

4. Crearemos una carpeta app donde colocaremos todo nuestro código de Flask.

5. Dentro de nuestra carpeta app, crearemos nuestro archivo main.py. En este tendremos nuestro código principal de Flask.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
    return "<h1>Hola desde Heroku!</h1>"
```

6. En nuestro directorio principal crearemos el archivo wsgi.py con el siguiente código.

```python
from app.main import app

if __name__ == "__main__":
    app.run()
```

7. Con pipenv ingresaremos a nuestro entorno virtual por medio de la consola.

```text
pipenv shell
```

8. Iniciaremos un repositorio vacío, agregaremos los archivos que hemos hecho y daremos commit a esos cambios, desde la consola.

```text
git init
git add .
git commit -m "Commit inicial"
```

9. Iniciaremos sesión utilizando el Heroku CLI en la consola.

```text
heroku login
```

Este nos pedirá que presionemos cualqueir tecla para iniciar sesión en nuestro navegador o q para salir. Presionaremos cualquier tecla.

Luego, crearemos nuestra aplicación de la siguiente manera

```text
heroku create NOMBRE_APP
```

10. Daremos push a nuestro código usando Heroku CLI.

```text
git push heroku master
```

Este comando nos mostrará distintos mensajes. Luego, al finalizar nos mostrará un mensaje de que ya esta listo nuestro despliegue.

```text
...
remote: -----> Launching...
remote:        Released v3
remote:        https://NOMBRE_APP.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
...
```

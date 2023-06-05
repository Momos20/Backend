# CRUD
## Comandos útiles

#### Para asegurar el correcto funcionamiento del código, sigue los siguientes pasos:

1.  Clona el repositorio de GitHub en tu máquina local
2.  Abre la terminal y navega hasta la ubicación del repositorio clonado. Utiliza el siguiente comando para acceder a la carpeta correspondiente:

```
  cd ruta-de-la-carpeta/flask-backend
```
3.  Ejecuta el siguiente comando para iniciar los contenedores de Docker en segundo plano:

```
  docker-compose up -d
```
4.  A continuación, ejecuta el siguiente comando para acceder a un contenedor de MySQL:	
```
docker-compose run --rm -v ${PWD}:/opt/src -w /opt/src mysql bash
```
Este comando abrirá una sesión de bash dentro del contenedor de MySQL.

5.  Una vez dentro del contenedor de MySQL, ejecuta el siguiente comando para crear la base de datos:
```
mysql -u companies -h mysql -p companies < ./db/creation.sql
```
Esto importará el script "creation.sql" y creará la base de datos necesaria para la aplicación.

6.  Después de crear la base de datos, puedes acceder a MariaDB ejecutando el siguiente comando:
```
mysql -u companies -h mysql -p
```
Se te solicitará ingresar la contraseña, que en este caso es "password".

Ahora estás listo para trabajar con la aplicación. Asegúrate de seguir las instrucciones adicionales proporcionadas en el repositorio o en la documentación para configurar y utilizar correctamente la aplicación Flask.

## Autores
- Sara Pérez Higuita
- Juan Camilo Cataño Zuleta


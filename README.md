# Challenge Backend<br>
Esta es la descripción del proyecto creado:<br>

Se utilizó Python 3.9.7 y Flask 2.2.2<br>

## Datos de la base de datos:
<u>user</u> = Flaviodc7<br>
<u>password</u> = RjhysU14audN<br>
<u>host</u> = ep-late-darkness-946800.us-east-2.aws.neon.tech<br>
<u>port</u> = 5432<br>
<u>database</u> = neondb<br>

## Metodos funcionales:

<u>Metodo:</u> GET<br>
<u>Ruta:</u> ./estaciones/<br>
<u>Descripción:</u> Devuelve todas las estaciones dentro de la base de datos

<u>Metodo:</u> GET<br>
<u>Ruta:</u> ./estaciones/<id><br>
<u>Descripción:</u> Devuelve la estación correspondiente al id ingresado

<u>Metodo:</u> POST<br>
<u>Ruta:</u> ./estaciones/add/<br>
<u>Descripción:</u> sirve para añadir una nueva estación en formato JSON, ingresando id, latitud y longitud

<u>Metodo:</u> DELETE<br>
<u>Ruta:</u> ./estaciones/delete/<id><br>
<u>Descripción:</u> Elimina la estación indicada en el id ingresado

<u>Metodo:</u> PUT<br>
<u>Ruta:</u> ./update/<br>
<u>Descripción:</u> modifica una estación ingresando los parametros en formato JSON.

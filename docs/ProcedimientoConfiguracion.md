# 1. Configuración Inicial del Repositorio
## Creación del Repositorio en GitHub

### Pasos para crear el repositorio remoto:

   1.	Se accedió al sitio GitHub.
![acceder_github](<imagenes/acceder_github.png>)
   2. Se inició sesión en la cuenta personal.
   3. Se hizo clic en el botón **"New"** para crear un nuevo repositorio.
![Punto2-3](<imagenes/Punto2-3.png>)
   4. Se configuró el repositorio con los siguientes datos:
   - **Nombre:** `Sabores_del_Valle`
   - **Descripción:** "Proyecto colaborativo para la creación de la carta digital de Sabores del Valle."
   - **Visibilidad:** Privado
   - No se inicializó con README.md
   5. Se hizo clic en **"Create repository"**.
![Punto4-5](<imagenes/Punto4-5.png>)

### Enlace al Repositorio Remoto
El repositorio es privado, por lo que el acceso está restringido a los miembros autorizados.

![enlacerepo](<imagenes/enlacerepo.png>)
- URL interna de referencia:
https://github.com/tu_usuario/Sabores_del_Valle.git
> *(Reemplazar tu_usuario por tu nombre real de usuario GitHub)



### Configuración del Entorno Local
Pasos para configurar el entorno de desarrollo local:

### Clonación del Repositorio
   1.	Desde GitHub, obtuvimos la URL del repositorio creado previamente. 

   2.	Abrimos la terminal, ejecutamos el siguiente comando para clonar el repositorio
![gitcmd](<imagenes/gitcmd.png)

![clonar_repo](<imagenes/clonar_repo.png)
   3.	Luego de clonar, accedimos a la carpeta local del repositorio:
![carpeta_git](imagenes/.png)

   4.	Abrimos Visual Studio Code y cargamos el repositorio clonado usando "File" > "Open Folder".
![vscode_carpeta](<imagenes/vscode_carpeta.png)



### Creación de archivo inicial y establecemos la rama main
Desde GitHub, obtuvimos la URL del repositorio creado previamente. 
   1.	Agrega algún archivo dentro del repositorio local
   ![readme](<imagenes/readme.png)
   2.	Agrega todos los archivos al área de staging
   ![add_readme](<imagenes/add_readme.png)
   3.	Haz tu primer commit
   ![commit_readme](<imagenes/commit_readme.png)
   4.	Ahora forzamos que la rama sea main
   ![forzamos_main](<imagenes/forzamos_main.png)
   5.	Finalmente sube main a GitHub
   ![push_readme](<imagenes/push_readme.png)


### Configuración de Ramas Principales y de Trabajo 
   1.	Crear la rama principal de desarrollo a partir de main y nos cambiamos a ella
   ![rama_develop](<imagenes/rama_develop.png)

   2.	Subir la rama develop al repositorio remoto dejándolo enlazado
   ![push_develop](<imagenes/push_develop.png)

   3.	Ubicarnos en la rama develop, si aún no estas ubicado.
   ![checkout_develop](<imagenes/checkout_develop.png)

   4.	Crear ramas de trabajo a partir de la rama develop y nos cambiamos a ella
   ![ramas_trabajo](<imagenes/.png)

   5.	Subir la rama de trabajo al repositorio remoto
   ![subir_rama_t.png](<imagenes/subir_rama_t.png)

   6.	Crear ramas de trabajo necesarias a partir de develop, cambiarnos a ellas y subirlos al repositorio remoto.
   ![crear_ramas_trabajo](<imagenes/crear_ramas_trabajo.png)

   7.	Cada rama de trabajo tiene una responsabilidad específica. 
   ![resp_rama](<imagenes/resp_rama.png)

   ![resp_rama_2](<imagenes/resp_rama_2.png)

enlace de youtube: https://www.youtube.com/watch?v=YZeNXU707EM

Sistema de Reservas de Hotel 🏨

Este es un proyecto de API RESTful desarrollado en Django REST Framework para gestionar reservas de hotel, incluyendo funcionalidades para habitaciones, clientes, reservas, reseñas y disponibilidad.

📋 Descripción
La API permite gestionar las operaciones básicas de un hotel, tales como:

CRUD completo para habitaciones y reservas.

Verificar la disponibilidad de habitaciones en un rango de fechas.

Crear y gestionar reseñas y calificaciones para las habitaciones.

Operaciones de creación, modificación y cancelación de reservas.

🚀 Características
Modelos
Habitación: Representa las habitaciones del hotel.

Cliente: Representa a los clientes del hotel.

Reserva: Representa las reservas de los clientes.

Reseña: Representa las reseñas de los clientes sobre las habitaciones.

Endpoints de la API
Habitaciones:

GET /api/habitaciones/: Listar todas las habitaciones.

POST /api/habitaciones/: Crear una nueva habitación.

GET /api/habitaciones/{id}/: Ver los detalles de una habitación.

PUT /api/habitaciones/{id}/: Actualizar una habitación.

DELETE /api/habitaciones/{id}/: Eliminar una habitación.

Reservas:

GET /api/reservas/: Listar todas las reservas.

POST /api/reservas/: Crear una nueva reserva.

GET /api/reservas/{id}/: Ver los detalles de una reserva.

PUT /api/reservas/{id}/: Modificar una reserva.

DELETE /api/reservas/{id}/: Cancelar una reserva.

Disponibilidad:

GET /api/disponibilidad/: Verificar la disponibilidad de habitaciones en un rango de fechas.

Reseñas:

GET /api/resenas/: Listar todas las reseñas.

POST /api/resenas/: Crear una nueva reseña.

⚙️ Requisitos
Para ejecutar este proyecto necesitas tener Python 3.8+ y Django instalado, así como las dependencias necesarias.

Instalar Python:
Asegúrate de tener Python 3.8 o superior. Puedes descargarlo desde python.org.

Instalar dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Configurar la base de datos:
La base de datos predeterminada es SQLite, lo que simplifica el proceso de configuración. Si quieres usar otra base de datos, actualiza el archivo settings.py en la sección de DATABASES.

🛠️ Instalación y Ejecución
Clonar el repositorio:

bash
Copiar
Editar
git clone https://github.com/tu_usuario/nombre_del_repositorio.git
Crear las migraciones y aplicar:

bash
Copiar
Editar
python manage.py migrate
Crear un superusuario (opcional para usar el admin):

bash
Copiar
Editar
python manage.py createsuperuser
Correr el servidor:

bash
Copiar
Editar
python manage.py runserver
La API estará disponible en http://127.0.0.1:8000/.

🔧 Pruebas con Thunder Client o Postman
Una vez que el servidor esté corriendo, puedes probar los endpoints usando herramientas como Thunder Client o Postman.

Ejemplo de cómo probar los endpoints:
Ver disponibilidad de habitaciones:
GET http://127.0.0.1:8000/api/disponibilidad/?fecha_inicio=2025-05-01&fecha_fin=2025-05-10

Crear una nueva reserva:
POST http://127.0.0.1:8000/api/reservas/
Con datos en el cuerpo de la solicitud (JSON).

📄 Base de Datos
Este proyecto usa SQLite como base de datos predeterminada. Los datos se almacenan en el archivo db.sqlite3, y puedes ver y manipular la base de datos con herramientas como DB Browser for SQLite o SQLite Viewer en Visual Studio Code.

📚 Documentación
Si deseas más detalles sobre cómo interactuar con cada endpoint de la API, puedes revisar los archivos de serializers y views en el directorio hotel_api/.

📄 Contribuciones
Si quieres contribuir al proyecto, por favor sigue estos pasos:

Forkea el repositorio.

Crea tu rama (git checkout -b feature/nueva-funcionalidad).

Haz los cambios y añade pruebas.

Realiza un commit con tus cambios (git commit -m 'Añadir nueva funcionalidad').

Push a tu rama (git push origin feature/nueva-funcionalidad).

Crea un pull request.


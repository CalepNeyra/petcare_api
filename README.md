---

## Evidencias de funcionamiento

A continuación se muestran capturas de prueba de los endpoints usando un cliente REST.

### Vista principal de la API

Se muestra la ruta principal de la API, donde aparecen los endpoints disponibles para dueños y mascotas.

![Vista principal de la API](fotos/p2-1%20(review).PNG)

---

### Creación de un dueño

Se realiza una petición `POST /duenos/` para registrar un nuevo dueño con su nombre y teléfono.

![Creación de dueño](fotos/p2-2%20(review).PNG)

---

### Creación de una mascota

Se realiza una petición `POST /mascotas/` para registrar una mascota asociada a un dueño mediante el campo `dueno`.

![Creación de mascota](fotos/p2-3%20(review).PNG)

---

### Listado de mascotas

Se realiza una petición `GET /mascotas/` para mostrar todas las mascotas registradas.  
Además, se visualiza la información personalizada del dueño mediante los campos `nombre_dueno` y `telefono_dueno`.

![Listado de mascotas](fotos/p2-8%20(review).PNG)

---

### Actualización de una mascota

Se realiza una petición `PATCH /mascotas/1/` para actualizar parcialmente la edad de una mascota.

![Actualización de mascota](fotos/p2-7%20(review).PNG)

---

### Búsqueda de mascota por nombre

Se realiza una petición `GET /mascotas/?search=Firulais` para buscar mascotas por nombre.

![Búsqueda por nombre](fotos/p2-5%20(review).PNG)

---

### Búsqueda de mascota por especie

Se realiza una petición `GET /mascotas/?search=Perro` para buscar mascotas por especie.

![Búsqueda por especie](fotos/p2-6%20(review).PNG)

---

### Eliminación de una mascota

Se realiza una petición `DELETE /mascotas/1/`, obteniendo una respuesta `204 No Content`, lo que indica que el registro fue eliminado correctamente.

![Eliminación de mascota](fotos/p2-4%20(review).PNG)

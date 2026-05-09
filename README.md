# PetCare API - Gestor de Mascotas

## Descripción breve del proyecto

PetCare API es una API REST desarrollada con Django y Django REST Framework.  
El proyecto permite administrar mascotas y dueños mediante endpoints REST, sin utilizar Django Admin como interfaz de gestión.

La API permite listar, crear, actualizar, buscar y eliminar mascotas. Además, cada mascota está relacionada con un dueño, permitiendo visualizar información del dueño dentro del JSON de la mascota.

---

## Tecnologías usadas

- Python
- Django
- Django REST Framework
- SQLite
- Git
- GitHub

---

## Instrucciones para ejecutar el servidor

### 1. Clonar el repositorio

```bash
git clone https://github.com/CalepNeyra/petcare_api.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd petcare_api
```

### 3. Crear un entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

En Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install django djangorestframework
```

### 6. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en:

```txt
http://127.0.0.1:8000/
```

---

## Endpoints disponibles

### Endpoints de Dueños

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/duenos/` | Lista todos los dueños registrados |
| POST | `/duenos/` | Crea un nuevo dueño |
| GET | `/duenos/{id}/` | Muestra un dueño específico |
| PUT | `/duenos/{id}/` | Actualiza completamente los datos de un dueño |
| PATCH | `/duenos/{id}/` | Actualiza parcialmente los datos de un dueño |
| DELETE | `/duenos/{id}/` | Elimina un dueño existente |

### Endpoints de Mascotas

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/mascotas/` | Lista todas las mascotas registradas |
| POST | `/mascotas/` | Crea una nueva mascota |
| GET | `/mascotas/{id}/` | Muestra una mascota específica |
| PUT | `/mascotas/{id}/` | Actualiza completamente los datos de una mascota |
| PATCH | `/mascotas/{id}/` | Actualiza parcialmente los datos de una mascota |
| DELETE | `/mascotas/{id}/` | Elimina una mascota existente |
| GET | `/mascotas/?search=texto` | Busca mascotas por nombre o especie |

---

## Ejemplos de uso

### Crear un dueño

**Método:** `POST`  
**Endpoint:** `/duenos/`

JSON enviado:

```json
{
    "nombre": "Carlos Perez",
    "telefono": "987654321"
}
```

Respuesta esperada:

```json
{
    "id": 1,
    "nombre": "Carlos Perez",
    "telefono": "987654321"
}
```

---

### Listar dueños

**Método:** `GET`  
**Endpoint:** `/duenos/`

Respuesta esperada:

```json
[
    {
        "id": 1,
        "nombre": "Carlos Perez",
        "telefono": "987654321"
    }
]
```

---

### Crear una mascota

**Método:** `POST`  
**Endpoint:** `/mascotas/`

JSON enviado:

```json
{
    "nombre": "Firulais",
    "especie": "Perro",
    "edad": 3,
    "dueno": 1
}
```

Respuesta esperada:

```json
{
    "id": 1,
    "nombre": "Firulais",
    "especie": "Perro",
    "edad": 3,
    "dueno": 1,
    "nombre_dueno": "Carlos Perez",
    "telefono_dueno": "987654321"
}
```

---

### Listar mascotas

**Método:** `GET`  
**Endpoint:** `/mascotas/`

Respuesta esperada:

```json
[
    {
        "id": 1,
        "nombre": "Firulais",
        "especie": "Perro",
        "edad": 3,
        "dueno": 1,
        "nombre_dueno": "Carlos Perez",
        "telefono_dueno": "987654321"
    }
]
```

---

### Actualizar una mascota

**Método:** `PATCH`  
**Endpoint:** `/mascotas/1/`

JSON enviado:

```json
{
    "edad": 4
}
```

Respuesta esperada:

```json
{
    "id": 1,
    "nombre": "Firulais",
    "especie": "Perro",
    "edad": 4,
    "dueno": 1,
    "nombre_dueno": "Carlos Perez",
    "telefono_dueno": "987654321"
}
```

---

### Buscar una mascota por nombre

**Método:** `GET`  
**Endpoint:** `/mascotas/?search=Firulais`

Este endpoint permite buscar una mascota por su nombre.

---

### Buscar una mascota por especie

**Método:** `GET`  
**Endpoint:** `/mascotas/?search=Perro`

Este endpoint permite buscar mascotas por especie.

---

### Eliminar una mascota

**Método:** `DELETE`  
**Endpoint:** `/mascotas/1/`

Respuesta esperada:

```txt
204 No Content
```

Esto indica que la mascota fue eliminada correctamente.

---

## Relación entre Mascota y Dueño

Cada mascota está relacionada con un dueño mediante el campo `dueno`.

Ejemplo:

```json
{
    "id": 1,
    "nombre": "Firulais",
    "especie": "Perro",
    "edad": 4,
    "dueno": 1,
    "nombre_dueno": "Carlos Perez",
    "telefono_dueno": "987654321"
}
```

En este ejemplo, la mascota `Firulais` pertenece al dueño `Carlos Perez`.

---

## Capturas de prueba de los endpoints

Las siguientes capturas muestran el funcionamiento de los endpoints desde un cliente REST.

### Vista principal de la API

![Vista principal de la API](fotos/p2-1%20(review).PNG)

---

### Creación de un dueño

![Creación de dueño](fotos/p2-2%20(review).PNG)

---

### Creación de una mascota

![Creación de mascota](fotos/p2-3%20(review).PNG)

---

### Eliminación de una mascota

![Eliminación de mascota](fotos/p2-4%20(review).PNG)

---

### Búsqueda de mascota por nombre

![Búsqueda por nombre](fotos/p2-5%20(review).PNG)

---

### Búsqueda de mascota por especie

![Búsqueda por especie](fotos/p2-6%20(review).PNG)

---

### Actualización de mascota

![Actualización de mascota](fotos/p2-7%20(review).PNG)

---

### Listado de mascotas

![Listado de mascotas](fotos/p2-8%20(review).PNG)

---

## Punto extra aplicado

Se personalizó la respuesta del endpoint de mascotas para mostrar información del dueño dentro del JSON de la mascota.

Campos agregados:

- `nombre_dueno`
- `telefono_dueno`

Esto permite visualizar datos del dueño directamente al consultar las mascotas.

---

## Autor

Calep Neyra

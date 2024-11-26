import requests

# URL base de la API
url_base = "http://127.0.0.1:5000/usuarios"

# 1. Crear un Usuario (POST)
def crear_usuario(nombre, edad):
    data = {
        "nombre": nombre,
        "edad": edad
    }
    response = requests.post(url_base, json=data)
    print("Crear Usuario:", response.json())

# 2. Obtener Todos los Usuarios (GET)
def obtener_usuarios():
    response = requests.get(url_base)
    print("Obtener Todos los Usuarios:", response.json())

# 3. Obtener un Usuario por ID (GET)
def obtener_usuario(id):
    response = requests.get(f"{url_base}/{id}")
    print(f"Obtener Usuario {id}:", response.json())

# 4. Actualizar un Usuario (PUT)
def actualizar_usuario(id, nombre, edad):
    data = {
        "nombre": nombre,
        "edad": edad
    }
    response = requests.put(f"{url_base}/{id}", json=data)
    print(f"Actualizar Usuario {id}:", response.json())

# 5. Eliminar un Usuario (DELETE)
def eliminar_usuario(id):
    response = requests.delete(f"{url_base}/{id}")
    print(f"Eliminar Usuario {id}:", response.json())

# Probar cada operación
if __name__ == "__main__":
    # Crear un nuevo usuario
    crear_usuario("Juan", 25)

    # Obtener todos los usuarios
    obtener_usuarios()

    # Obtener un usuario específico por ID
    obtener_usuario(1)

    # Actualizar el usuario con ID 1
    actualizar_usuario(1, "Juan Actualizado", 26)

    # Obtener el usuario actualizado
    obtener_usuario(1)

    # Eliminar el usuario con ID 1
    eliminar_usuario(1)

    # Intentar obtener el usuario eliminado
    obtener_usuario(1)
@app.route('/')
def index():
    return "Bienvenido a la API"

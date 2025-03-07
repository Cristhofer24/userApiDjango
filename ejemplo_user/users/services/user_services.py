import requests
from ..models import UserProfile

API_URL = "https://randomuser.me/api/?page=3&results=10&seed=abc"

def get_users():
    # Realiza la solicitud a la API
    response = requests.get(API_URL)
    
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Accede a los resultados de la API
        return response.json().get("results", [])
    return []

def get_user(id):
    response = requests.get(f"{API_URL}/{id}")
    if response.status_code == 200:
        return response.json().get("results", [])
    return[]

def load_user():
    # Verifica si no hay usuarios en la base de datos
    if not UserProfile.objects.count():
        users = get_users()  # Obtiene los usuarios desde la API

        # Si la lista de usuarios está vacía, no continúa
        if not users:
            return "No se encontraron usuarios en la API"

        # Itera sobre los usuarios obtenidos de la API
        for user_data in users:
            # print(user_data)  # Imprime el contenido de cada 'user_data' para verificar la estructura.

            # Crea un nuevo usuario en la base de datos
            UserProfile.objects.create(
                gender=user_data.get("gender", ""),
                title=user_data["name"].get("title", ""),
                first_name=user_data["name"].get("first", ""),
                last_name=user_data["name"].get("last", ""),
                street_number=user_data["location"]["street"].get("number", ""),
                street_name=user_data["location"]["street"].get("name", ""),
                city=user_data["location"].get("city", ""),
                state=user_data["location"].get("state", ""),
                country=user_data["location"].get("country", ""),
                postcode=user_data["location"].get("postcode", ""),
                latitude=user_data["location"]["coordinates"].get("latitude", ""),
                longitude=user_data["location"]["coordinates"].get("longitude", ""),
                timezone_offset=user_data["location"]["timezone"].get("offset", ""),
                timezone_description=user_data["location"]["timezone"].get("description", ""),
                email=user_data.get("email", ""),
                username=user_data["login"].get("username", ""),
                password_hash=user_data["login"].get("md5", ""),
                dob=user_data["dob"].get("date", "")[:10],
                age=user_data["dob"].get("age", 0),
                phone=user_data.get("phone", ""),
                cell=user_data.get("cell", ""),
                ssn=user_data["id"].get("value", ""),
                picture_url=user_data["picture"].get("large", ""),
                nationality=user_data.get("nat", "")
            )

        return f"{len(users)} Usuarios cargados"  # Esto se debe ejecutar después de haber cargado todos los usuarios.
    return "Usuarios ya cargados"  # Si ya hay usuarios, no carga más.

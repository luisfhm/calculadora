from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()  # carga las variables de entorno del .env

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Variables de entorno SUPABASE_URL y SUPABASE_KEY no están definidas")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def guardar_email(email: str) -> bool:
    try:
        response = supabase.table("emails").insert({"email": email}).execute()
        print("Respuesta completa:", response)
        print("Datos guardados:", response.data)
        # Como el email sí se guardó, asumamos que si response.data no es vacío, fue exitoso
        if response.data:
            return True
        else:
            print("No se guardó el email o la respuesta no tiene datos")
            return False
    except Exception as e:
        print("Exception guardando email:", e)
        return False



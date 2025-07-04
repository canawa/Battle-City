from fastapi import FastAPI
from supabase import create_client, Client
import dotenv
import os

dotenv.load_dotenv() # загружаем переменные окружения из .env файла (в проде не надо)
url: str = os.environ.get("SUPABASE_URL") # надо будет добавить в ~bashrc на убунту серваке
key: str = os.environ.get("SUPABASE_KEY") # надо будет добавить в ~bashrc на убунту серваке
supabase: Client = create_client(url, key)
app = FastAPI() 

@app.get("/api/userInfo/{userName}") # динамический параметр, который будет передаваться в функцию. Потом сделаем так чтобы с админки можно было посмотреть информацию о всех пользователях
def hello(userName: str):  # функция, которая будет возвращать информацию о пользователе
    return {"message": f"Добро пожаловать, {userName}!",    
     'userBalance': 'баланс пользователя (запрос supabase)',
     'registrationDate': 'запрос регистрации (supabase)',
     'cashoutAmount':'выведено в стим (запрос supabase)'} # возвращаемые данные



 
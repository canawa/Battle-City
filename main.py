from fastapi import FastAPI, Depends
from supabase import create_client, Client
import dotenv
from pydantic import BaseModel, Field, EmailStr
import os
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


dotenv.load_dotenv() # загружаем переменные окружения из .env файла (в проде не надо)
url: str = os.environ.get("SUPABASE_URL") # надо будет добавить в ~bashrc на убунту серваке
service_key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") # надо будет добавить в ~bashrc на убунту серваке
anon_key: str = os.environ.get("SUPABASE_ANON_KEY") # для регистрации пользователей используем ANON_KEY

supabase_admin: Client = create_client(url, service_key)
supabase_anon: Client = create_client(url, anon_key)



app = FastAPI() 


class RegisterSchema(BaseModel):
    login: EmailStr
    password: str = Field(min_length=8, max_length=20)

@app.post('/api/register')
def register(user_data: RegisterSchema): #приходящий объект назовем user_data, и потом можно в него углубляться и вытаскивать данные
    try:
        response = supabase_anon.auth.sign_up( # используем метод (функцию) supabase.auth.sign_up для регистрации (от анонимного ключа, потому что от админки не идет письмо на почту)
        {
            'email': user_data.login, # передаем данные из объекта user_data в функцию supabase.auth.sign_up
            'password': user_data.password, # передаем данные из объекта user_data в функцию supabase.auth.sign_up
            
        }
        )
        return response
    except Exception as e:
        return {'error': str(e)}

@app.post('/api/login')
def login(user_data: RegisterSchema):
    try:
        response = supabase_anon.auth.sign_in_with_password(
            {
                'email': user_data.login,
                'password': user_data.password
            }
        )
        return response
    except Exception as e:
        return {'error': str(e)}


class ForgotPasswordSchema(BaseModel):
    emailValue: EmailStr


@app.post('/api/forgotpassword')
def forgot_password(email: ForgotPasswordSchema):
    try:    
        response = supabase_admin.auth.reset_password_for_email(email.emailValue,
        {
            'redirect_to': 'http://localhost:5173/#/resetpassword'  # перенаправление на страницу сброса пароля (это после нажатия на кнопку в письме, а не сразу)
        })
        if response == None:
            return {'status': 'Email was sent'} 
        return response # ничего не возвращает, потому что отправляется письмо на почту, и если письмо отправлено, то возвращается 200
    except Exception as e:
        return {'error': str(e)}


class ResetPasswordSchema(BaseModel):
    newPassword: str

@app.post('/api/resetpassword')
def reset_password(password: ResetPasswordSchema):
    try:
        response = supabase_admin.auth.update_user(
            {
                'password': password.newPassword
            }
        )
        print(response)
        return response
    except Exception as e:
        return {'error': str(e)}



@app.get('/api/checkifloggedin')
def check_if_logged_in(jwt_token: HTTPAuthorizationCredentials = Depends(HTTPBearer())): # Depends(HTTPBearer()) - это зависимость, которая позволяет получить токен из заголовков запроса (и передает в jwt_token как credentials)
    try:
        response = supabase_admin.auth.get_user(jwt_token.credentials) # получаем информацию о пользователе (в credentials лежит токен - благодаря Depends(HTTPBearer()) мы его получили)
        print(response)
        return response
    except Exception as e:
        return {'error': str(e)}
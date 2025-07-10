from fastapi import FastAPI, Depends
from supabase import create_client, Client
import dotenv
from pydantic import BaseModel, Field, EmailStr
import os
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

dotenv.load_dotenv() # загружаем переменные окружения из .env файла (в проде не надо)
url: str = os.environ.get("SUPABASE_URL") # надо будет добавить в ~bashrc на убунту серваке
service_key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") # надо будет добавить в ~bashrc на убунту серваке
anon_key: str = os.environ.get("SUPABASE_ANON_KEY") # для регистрации пользователей используем ANON_KEY
jwt_secret: str = os.environ.get("SUPABASE_JWT_SECRET")

supabase_admin: Client = create_client(url, service_key)
supabase_anon: Client = create_client(url, anon_key)



app = FastAPI() 



@app.post('/api/logout')
def logout():
    try:
        response = supabase_admin.auth.sign_out()
        return response
    except Exception as e:
        return {'error': str(e)}

class RegisterSchema(BaseModel):
    login: EmailStr
    password: str = Field(min_length=8, max_length=20)

@app.post('/api/register')
def register(user_data: RegisterSchema): #приходящий объект назовем user_data, и потом можно в него углубляться и вытаскивать данные
    try:
        response = supabase_anon.auth.sign_up ( # используем метод (функцию) supabase.auth.sign_up для регистрации (от анонимного ключа, потому что от админки не идет письмо на почту)
        {
            'email': user_data.login, # передаем данные из объекта user_data в функцию supabase.auth.sign_up
            'password': user_data.password, # передаем данные из объекта user_data в функцию supabase.auth.sign_up
            'options': {
                'email_redirect_to': 'http://localhost:5173/#/login' # ублюдский синтаксис, но так надо, меняет ссылку на которую перекинет после подтверждения почты
            }    
        },

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
    try: # приходит токен, мы его записываем как jwt_token
        response = supabase_admin.auth.get_user(jwt_token.credentials)
        print(response) # получаем информацию о пользователе (в credentials лежит токен - благодаря Depends(HTTPBearer()) мы его получили)
        if response.user or response.session:
            return {'user': True}
        else:
            return {'user': False}
        
    except Exception as e:
        return {'error': str(e)}


@app.get('/api/getuserbalance')
def balance(jwt_token: HTTPAuthorizationCredentials = Depends(HTTPBearer())): 
    token = jwt_token.credentials # токен есть, но теперь его надо распарсить, чтобы вытащить информацию 
    decoded_token = jwt.decode(token, jwt_secret, algorithms=["HS256"], audience="authenticated") # расшифровываем токен, чтобы получить информацию о пользователе
    uuid = decoded_token['sub'] # получаем uuid пользователя (почему именно так? потому что jwt.decode возвращает словарь, а не объект, поэтому по ключу ищем 'sub')
    print(uuid)
    response = (
        supabase_admin.table('users') # из таблицы users 
        .select('balance') # выбираем поле balance
        .eq('auth_user_id', uuid) # ищем пользователя по auth_user_id 
        .execute() # выполняем запрос (а не просто описываем его)
    )
    print(response)
    return response
    
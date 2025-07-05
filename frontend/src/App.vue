<script setup> // можно просто писать js код, без экспорта
import { ref } from 'vue' // ref - это функция из vue, которая позволяет создавать реактивные переменные (изменив их можно не перезагружать страницу чтобы увидеть результат) 


const errorMessage = ref('')



const registerProcess = async () => {
  const login = document.getElementById('login-input').value
  const password = document.getElementById('password-input').value
  const response = await fetch('/api/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ login, password })
  })
  const data = await response.json()
  console.log(data)
  if (data.error == true) {
    errorMessage.value = data.error
  } else {
    errorMessage.value = 'Успешно зарегистрированы! Подтвердите почту!'
  }
}

const loginProcess = async () => {
  const login = document.getElementById('login-input').value
  const password = document.getElementById('password-input').value
  const response = await fetch('/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ login, password })
  })
  const data = await response.json()
  console.log(data)
  if (data.error == true) {
    errorMessage.value = data.error
  } else {
    errorMessage.value = 'Успешно вошли в аккаунт!'
  }
}

</script>

<template>
<div id="main-container">

  <div id="header">
    <div id="header-logo">
    
      <img src="/src/assets/logo.png" alt="logo" id="logo"> <!-- logo - это переменная, которая лежит в App.vue. Переменные из script передаются в template через {{ }} -->
    
    </div>

    <div id="header-auth-buttons">
      <button type="button" id="header-login-button">  Sign in  </button> <!-- в vue js юзаем @click и потом метод, функцию, которая будет выполняться при нажатии на кнопку-->
      <button type="button" id="header-register-button">  Create Account  </button> <!-- в vue js юзаем @click и потом метод, функцию, которая будет выполняться при нажатии на кнопку-->

    </div>
  </div>

  <div id="register-form">
    
    <h2>Зарегистрироваться</h2>
    <input type="email" id="login-input" placeholder="Почта">
    <input type="password" id="password-input" placeholder="Пароль">
    <button type="button" id="login-button" @click = 'registerProcess()' > Зарегистрироваться </button>
  
  </div>

  <div id="login-form">
    
    <h2>Войти</h2>
    <input type="email" id="login-input" placeholder="Почта">
    <input type="password" id="password-input" placeholder="Пароль">
    <button type="button" id="login-button" @click = 'loginProcess()' > Войти </button>
  
  </div>
  
  <div id="error-message">
  
    <p>{{ errorMessage }}</p>
  
  </div>

</div>
</template>

<style scoped> /* стили для всего что лежит в App.vue */

#logo {
  width: 6%;
}

#main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
  height: 100vh;
  padding: 0 1%;

}



#header { /* стили для div с id logo */
  display: flex;
  color: white;
  width: 100%;
  height: 8%;
  font-family: 'Inter', sans-serif;
  align-items: center;
  justify-content: space-between;
  background-color: #12192b;
  border-radius: 1rem;
}

#header-auth-buttons {
  display: flex;
  align-items: center;
  justify-content: right;
  font-size: 1.2rem;
  margin-right: 1.5%;
  width: 15%;
  height: 100%;
  /* border: 2px solid white; */
}


#header-register-button {
  display: flex;
  align-items: center;
  cursor: pointer;
  color: white;
  background-color: #09a24e;
  transition: background-color 0.3s ease;
  border-radius: 10px;
  height: 50%;
  border: none;
  
}

#header-register-button:hover {
  background-color: #29ba67;
}

#header-login-button {
  display: flex;
  align-items: center;
  cursor: pointer;
  color: white;
  background-color: #1e2841;
  transition: background-color 0.3s ease;
  border-radius: 10px;
  height: 50%;
  padding: 0 4%;
  margin-right: 2%;
  border: none;
}

</style>

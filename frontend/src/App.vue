<script setup> // можно просто писать js код, без экспорта
import { ref } from 'vue' // ref - это функция из vue, которая позволяет создавать реактивные переменные (изменив их можно не перезагружать страницу чтобы увидеть результат) 

const loginText = ref('Войти / Зарегистрироваться')
const logo = ref('Battle City') // logo - это переменная, которая лежит в App.vue. Переменные из script передаются в template через {{ }}

const loginButton = () => {
  loginText.value = 'Влетаем в битву!' // когда оборачиваем переменную в ref, то мы можем использовать .value чтобы изменить ее значение, выглядит это так {value: 'наш текст'}, поэтому мы пишем loginText.value = 'наш текст'
}

const loginProcess = async () => {
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
}

</script>

<template>
  <div id="header">

    <h1>{{ logo }}</h1> <!-- logo - это переменная, которая лежит в App.vue. Переменные из script передаются в template через {{ }} -->
    <button type="button" id="login-button" @click = 'loginButton()' > {{ loginText }}  </button> <!-- в vue js юзаем @click и потом метод, функцию, которая будет выполняться при нажатии на кнопку-->
  </div>

  <div id="login-form">
    <input type="email" id="login-input" placeholder="Почта">
    <input type="password" id="password-input" placeholder="Пароль">
    <button type="button" id="login-button" @click = 'loginProcess()' > Зарегистрироваться </button>
  </div>

</template>

<style scoped> /* стили для всего что лежит в App.vue */

#header { /* стили для div с id logo */
  display: flex;
  color: green;
  justify-content: left;
  font-size: 20px;
  border: 1px solid black;
  font-family: 'Press Start 2P', cursive;
}

#login-button {
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

#login-button:hover {
  background-color: #00ff00;
  justify-content: right;
  border: 1px solid black;
  font-size: 20px;
  font-family: 'Press Start 2P', cursive;
  
}

</style>

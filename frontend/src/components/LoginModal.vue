<script setup>
import { ref } from 'vue'
const errorMessage = ref('')

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
<div id="login-form-modal-container" @click="$emit('closeLogin')" >
    <div id="login-form-modal-content" @click.stop>
      
    <h2>Войти</h2>
    <input type="email" id="login-input" placeholder="Почта">
    <input type="password" id="password-input" placeholder="Пароль">
    <button type="button" id="login-button" @click = 'loginProcess()' > Войти </button>

    </div>
</div>
</template>

<style scoped>
#login-form-modal-container {
 
    width: 100vw;
    height: 100vh;
    border: 1px solid red;
    display: flex;
    justify-content: center;
    align-items: center;
}
#login-form-modal-content {
  background-color: white;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    width: 50vw;
    height: 50vh;
    display: flex;
    flex-direction: column;
    border-radius: 15px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
    color: white;
    font-family: 'Manrope', sans-serif;
    font-weight: 600;
}
</style>
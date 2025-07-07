<script setup>
import { ref } from 'vue' // ref - это функция из vue, которая позволяет создавать реактивные переменные (изменив их можно не перезагружать страницу чтобы увидеть результат) 
import {useRouter} from 'vue-router' // импортируем из vue-router, которая позволяет переходить на другую страницу
import RegisterModal from './RegisterModal.vue'
import LoginModal from './LoginModal.vue'
import ForgotPasswordModal from './ForgotPasswordModal.vue'
const router = useRouter() // это функция из vue-router, которая позволяет переходить на другую страницу
const errorMessage = ref('')
const isLoggedIn = ref(false)
let showRegisterModal = ref(false)
let showLoginModal = ref(false)
let showForgotPasswordModal = ref(false)

const logout = async () => {
  const response = await fetch('/api/logout', {
    method: 'POST',
   
  })
  const data = await response.json()
  console.log(data)
  if (response.ok) {
    console.log('Successfully logged out')
    localStorage.removeItem('access_token')
    location.reload()
  }
  else {
    console.log('Failed to logout')
  }
}



const checkIfLoggedIn = async () => {
  const token = localStorage.getItem('access_token')
  const response = await fetch('/api/checkifloggedin', {
    headers: {
      'Authorization': `Bearer ${token}` // отправляет токен в строке запроса (стандратная форма такая просто удобно и очень безопасно)
    }
  })

  const data = await response.json()

  console.log(data)

  if (data.error) {
    console.log('not logged in')
  }
  else {
    console.log('logged in')
  }

  if (data.user || data.session) {
    isLoggedIn.value = true
    router.push('/')
  }
  else {
    isLoggedIn.value = false
  }


}
checkIfLoggedIn()



</script>

<template>

<div id="header"  @click="showLoginModal = false, showRegisterModal = false">
    <div id="header-logo">
    
      <img src="/src/assets/logo.png" alt="logo" id="logo" @click="router.push('/')"> <!-- logo - это переменная, которая лежит в App.vue. Переменные из script передаются в template через {{ }} -->
    
    </div>


    <div id="header-logout-button" >  
      <button type="button" id="header-logout-button" @click="logout">  Logout  </button>
    </div>
    <div id="header-auth-buttons" @click.stop v-if="!isLoggedIn" >  <!-- в template vue-js автоматически разворачивает ref, поэтому можно не писать про .value -->
<!-- Не пиши == true или == false, пиши просто !isLoggedIn  или isLoggedIn  потому что vue если написать через === то будет сравнение с ref объектом, а не с булевым значением внутри ref-->
      
      <button type="button" id="header-login-button" @click="showLoginModal = true, showRegisterModal = false">  Login  </button> <!-- в vue js юзаем @click и потом метод, функцию, которая будет выполняться при нажатии на кнопку-->
      <button type="button" id="header-register-button" @click="showRegisterModal = true, showLoginModal = false">  Create Account  </button> <!-- в vue js юзаем @click и потом метод, функцию, которая будет выполняться при нажатии на кнопку-->

    </div>
  </div>  
  <LoginModal v-if="showLoginModal" @closeLogin="showLoginModal = false" @openRegister="showRegisterModal=true, showLoginModal=false" @openForgotPassword="showForgotPasswordModal = true"/>
  <ForgotPasswordModal v-if="showForgotPasswordModal" @closeForgotPassword="showForgotPasswordModal = false" @openLogin="showLoginModal = true, showForgotPasswordModal = false"/>
  <RegisterModal v-if="showRegisterModal" @close="showRegisterModal = false" @openLogin="showLoginModal = true, showRegisterModal = false"/> <!-- этот компонент будет отображаться только если showModal.value === true -->
  <!-- Если прихоидит от RegisterModal событие через $emit('close') = false то showModal = false -->
<!-- Это метод обмена инфой от дочернего элемента (RegisterModal) к родительскому элементу (header) в котором лежит showModal-->


  <div id="error-message">
  
    <p>{{ errorMessage }}</p>
  
  </div>

</template>

<style scoped>


#logo {
  width: 10vh; /* 10vh - это 10% от высоты экрана (ДА ВСЕ ПРАВИЛЬНО, ВЫСОТЫ ДЛЯ ШИРИНЫ, ПОТОМУ ЧТО НИКТО НЕ СЖИМАЕТ ЭКРАН ПО ВЕРТИКАЛИ)*/

} 



#header { /* стили для div с id logo */
  display: flex;
  color: white;
  width: 100%;
  height: 8%;
  font-family: 'Manrope', sans-serif;
  font-weight: 600;
  align-items: center;
  justify-content: space-between;
  background-color: #12192b;
  border-radius: 1rem;
}

#header-auth-buttons {
  display: flex;
  align-items: center;
  justify-content: right;
  font-size: 1rem;
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
  border-radius: 0.5rem;
  height: 4vh;
  border: none;
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.5);
  
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
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.5);
  border-radius: 0.5rem;
  height: 4vh;
  padding: 0 1vh;
  margin-right: 1vh;
  border: none;
}



</style>
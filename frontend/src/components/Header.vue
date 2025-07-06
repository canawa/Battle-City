<script setup>
import { ref } from 'vue' // ref - это функция из vue, которая позволяет создавать реактивные переменные (изменив их можно не перезагружать страницу чтобы увидеть результат) 
import {useRouter} from 'vue-router' // импортируем из vue-router, которая позволяет переходить на другую страницу
import RegisterModal from './RegisterModal.vue'
import LoginModal from './LoginModal.vue'
const router = useRouter() // это функция из vue-router, которая позволяет переходить на другую страницу
const errorMessage = ref('')

let showRegisterModal = ref(false)
let showLoginModal = ref(false)
</script>

<template>

<div id="header"  @click="showLoginModal = false, showRegisterModal = false">
    <div id="header-logo">
    
      <img src="/src/assets/logo.png" alt="logo" id="logo"> <!-- logo - это переменная, которая лежит в App.vue. Переменные из script передаются в template через {{ }} -->
    
    </div>

    <div id="header-auth-buttons" @click.stop>  
      <button type="button" id="header-login-button" @click="showLoginModal = true, showRegisterModal = false">  Login  </button> <!-- в vue js юзаем @click и потом метод, функцию, которая будет выполняться при нажатии на кнопку-->
      <button type="button" id="header-register-button" @click="showRegisterModal = true, showLoginModal = false">  Create Account  </button> <!-- в vue js юзаем @click и потом метод, функцию, которая будет выполняться при нажатии на кнопку-->

    </div>
  </div>  
  <LoginModal v-if="showLoginModal" @closeLogin="showLoginModal = false" @openRegister="'showRegisterModal=true,'"/>
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
  border-radius: 0.5rem;
  height: 4vh;
  padding: 0 1vh;
  margin-right: 1vh;
  border: none;
}



</style>
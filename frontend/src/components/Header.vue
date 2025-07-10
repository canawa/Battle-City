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
let showUserDropdown = ref(false) // новое состояние для выпадающего меню
let userDropdownMenu = ref(false)

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

const toggleUserDropdown = () => {
  showUserDropdown.value = !showUserDropdown.value
}

const closeUserDropdown = () => {
  showUserDropdown.value = false
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


    <div id="header-logged-in-user" v-if="isLoggedIn"> 
      

      <div> <img src="@/assets/user_icon.png" alt="user-icon" id="user-icon" @click="userDropdownMenu = !userDropdownMenu" > </div> 
      <div id="user-dropdown-menu" v-if="userDropdownMenu"> 
        <div id="user-dropdown-menu-row">Profile</div>
        <div id="user-dropdown-menu-row">placeholder</div>
        <div id="user-dropdown-menu-row">placeholder</div>
        <div id="user-dropdown-menu-row">placeholder</div>
        <div id="user-dropdown-menu-last-row" @click="logout()">Logout</div>


      </div>
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

#user-dropdown-menu-row { /* стили для каждой строки выпадающего меню кроме последней*/
  display: flex;
  align-items: center;
  justify-content: center;
  color: #767678;
  font-size: 0.8rem;
  font-weight: 600;
  height: 19.5%;
  width: 100%;
  border-bottom: 1px solid #767678;
  cursor: pointer;

}

#user-dropdown-menu-last-row { /* стили для каждой строки выпадающего меню кроме последней*/
  display: flex;
  align-items: center;
  justify-content: center;
  color: #767678;
  font-size: 0.8rem;
  font-weight: 600;
  height: 19.5%;
  width: 100%;
  cursor: pointer;


}

#user-dropdown-menu-row:hover {
  background-color: #76767836;
}


#user-dropdown-menu {
  position: absolute;
  margin-top: 190px;
  background-color: whitesmoke;
  border-radius: 0.5rem;
  height: 150px;
  width: 100px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5); /* тень 0 смещение по оси x, 0 смещение по оси y, 10px blur, 0 растяжение тени по ширине (spread), это смещение! */
}

#user-icon {
  height: 4vh; /* 2% от высоты экрана, как у логотипа */
  margin-right: 0.8rem;
  cursor: pointer;
  transition: transform 0.3s ease, filter 0.3s ease;
}

#user-icon:hover {
  transform: scale(1.1);
  filter: brightness(1.2);
}

#logo {
  width: 10vh; /* 10vh - это 10% от высоты экрана (ДА ВСЕ ПРАВИЛЬНО, ВЫСОТЫ ДЛЯ ШИРИНЫ, ПОТОМУ ЧТО НИКТО НЕ СЖИМАЕТ ЭКРАН ПО ВЕРТИКАЛИ)*/
  margin-right: 1rem
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

#header-logged-in-user {
  display: flex;
  align-items: center;
  justify-content: right;
  flex-direction: row;
 
  width: 8%;
  height: 100%;
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
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
  console.log('Response data:', data)
  
  // Проверяем статус ответа
  if (data.error) {
    errorMessage.value = data.error
  }
  else if (data.detail && data.detail[0].type == 'value_error') { // ошибки возвращаются в виде массива, поэтому data.детали.[позиция в массиве (обычно 0)].type == 'string_too_long'
    errorMessage.value = 'Email is not valid'
  }
  else if (data.detail && data.detail[0].type == 'string_too_short') { // ошибки возвращаются в виде массива, поэтому data.детали.[позиция в массиве (обычно 0)].type == 'string_too_long'
    errorMessage.value = 'Password is too short'
  }
  else if (data.detail && data.detail[0].type == 'string_too_long') { // ошибки возвращаются в виде массива, поэтому data.детали.[позиция в массиве (обычно 0)].type == 'string_too_long'
    errorMessage.value = 'Password is too long'
  }
   else {
    errorMessage.value = 'Successfully logged in!'
  }
}
// ОБРАБОТЧИК ОШИБОК АУТЕНТИФИКАЦИИ

</script>

<template>
<div id="login-form-modal-container" @click="$emit('closeLogin')" >
    <div id="login-form-modal-content" @click.stop>
      <div id="login-form-modal-content-image">
        <img src="@/assets/battleCityBanner.png" alt="login-background" id="battle-city-banner-image" >


      </div>
      <div id="login-form-modal-content-form">

    <h2 id='login-title'>Log in</h2>
    <input type="email" id="login-input" placeholder="Enter your email">
    <input type="password" id="password-input" placeholder="Enter your password">
    <button type="button" id="login-button" @click="loginProcess()">Login</button>
    
    <!-- Сообщения об ошибках и успехе -->
    <div v-if="errorMessage" :class="errorMessage.includes('Successfully') ? 'success-message' : 'error-message'"> <!-- Тут чутка непонятно, но вроде как если в errorMessage будет Successfully, то будет success-message класс, а если нет, то error-message класс-->
      {{ errorMessage }}
    </div>
    
    <!-- Дополнительные ссылки -->
    <div class="additional-links">
      <div class="forgot-password">
        <a href="#" class="link-text" @click="$emit('openForgotPassword')">Forgot password?</a>
      </div>
      <div class="register-link">
        <span class="register-text">You don't have an account? </span>
        <a href="#" class="link-text highlighted" @click="$emit('openRegister')">Create account</a>
      </div>
    </div>
  
  </div>
    </div>
</div>
</template>

<style scoped>
#login-form-modal-content-image {
  width: 25vw;
  height: 100vh;
  display: flex;
  margin: 1rem;
  align-items: center;
  
}

#login-form-modal-container {
    position: fixed; /* чтобы модальное окно было поверх всех элементов (его нельзя сместить)*/
    z-index: 1000; /* чтобы модальное окно было выше всех элементов*/
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(10px);
    background-color: rgba(0, 0, 0, 0.5);
    
  }
#login-form-modal-content {
  background-color: #121929;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 45vw;
  height: 70vh;
  display: flex;
  flex-direction: row;
  border-radius: 1rem;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
  color: #0d111b;
  background-color: #121929;
  font-family: 'Manrope', sans-serif;
  font-weight: 600;
  animation: modalSlideIn 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
@media (max-width: 768px) {
  #login-form-modal-content {
    height: 30vh;
    flex-direction: column;
  }
}

#battle-city-banner-image {
  display: flex;
  width: 21.5vw;
  border-radius: 1rem;
}
@media (max-width: 768px) {
  #battle-city-banner-image {
    content: url('@/assets/battleCityBannerMobile.png');
    width: 100%;
  }
}
#login-form-modal-content-form {
  width: 30vw;
  height: 70vh;
  
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  padding: 2rem;
}

@media (max-width: 768px) {
  #battle-city-banner-image{
    height: 30vh;
    border-radius: 1rem;
    
  }
}

#login-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: white;
  font-family: 'Manrope', sans-serif;
  margin-bottom: 1rem;
  text-align: center;
}

/* Стили для input полей */
#login-input, #password-input {
  width: 100%;
  max-width: 300px;
  padding: 1rem 1.5rem;
  font-size: 1rem;
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05);
  color: white;
  font-family: 'Manrope', sans-serif;
  font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

#login-input::placeholder, #password-input::placeholder {
  color: rgba(255, 255, 255, 0.6);
  font-weight: 400;
}

#login-input:focus, #password-input:focus {
  outline: none;
  border-color: #667eea;
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1), 0 8px 25px rgba(0, 0, 0, 0.2);
  transform: translateY(-2px);
}

#login-input:hover, #password-input:hover {
  border-color: rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.08);
  transform: translateY(-1px);
}

/* Стили для кнопки */
#login-button {
  width: 100%;
  max-width: 300px;
  padding: 1rem 0rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none; 
  border-radius: 12px;
  cursor: pointer;
  font-family: 'Manrope', sans-serif;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
  position: relative;
  overflow: hidden;
}

#login-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

#login-button:hover::before {
  left: 100%;
}

#login-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
}

#login-button:active {
  transform: translateY(-1px);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

/* Сообщение об ошибке */
.error-message {
  color: #ff6b6b;
  font-size: 0.9rem;
  font-weight: 500;
  text-align: center;
  margin-top: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(255, 107, 107, 0.1);
  border-radius: 8px;
  border: 1px solid rgba(255, 107, 107, 0.2);
  animation: fadeIn 0.3s ease-in-out;
}

.success-message {
  color: #51cf66;
  font-size: 0.9rem;
  font-weight: 500;
  text-align: center;
  margin-top: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(81, 207, 102, 0.1);
  border-radius: 8px;
  border: 1px solid rgba(81, 207, 102, 0.2);
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(-20px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

/* Стили для дополнительных ссылок */
.additional-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 300px;
}

.forgot-password {
  text-align: center;
}

.register-link {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.register-text {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  font-weight: 400;
  margin-top: 1rem;
  font-family: 'Manrope', sans-serif;
}

.link-text {
  color: #667eea;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  font-family: 'Manrope', sans-serif;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  cursor: pointer;
}



.link-text:hover {
  color: #5a6fd8;
  transform: translateY(-1px);
}

.link-text.highlighted {
  color: #764ba2;
  font-weight: 600;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.link-text.highlighted:hover {
  background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Адаптивные стили для мобильных устройств */
@media (max-width: 768px) {
  #login-form-modal-content {
    width: 85vw !important;
    min-height: 60vh !important;
    max-height: 80vh !important;
    flex-direction: column !important;
    padding: 1rem;
  }
  
  #login-form-modal-content-image {
    width: 100% !important;
    height: 25vh !important;
    min-height: 200px !important;
    max-height: 300px !important;
    margin: 0 !important;
    justify-content: center;
    align-items: center;
  }
  
  #battle-city-banner-image {
    width: 100% !important;
    max-width: 400px !important;
    height: auto !important;
    object-fit: contain !important;
  }
  
  #login-form-modal-content-form {
    width: 100% !important;
    flex: 1 !important;
    min-height: 35vh !important;
    justify-content: center !important;
    padding: 1rem !important;
    gap: 1rem;
  }
  
  #login-title {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }
  
  #login-input, #password-input {
    max-width: 90%;
    padding: 0.8rem 1rem;
    font-size: 0.9rem;
  }
  
  #login-button {
    max-width: 100%;
    padding: 0.8rem 0;
    font-size: 1rem;
  }
  
  .additional-links {
    max-width: 100%;
    gap: 0.5rem;
  }
  
  .register-text {
    font-size: 0.8rem;
  }
  
  .link-text {
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  #login-form-modal-content {
    width: 90vw !important;
    min-height: 70vh !important;
    max-height: 85vh !important;
  }
  
  #login-form-modal-content-image {
    height: 25vh !important;
    min-height: 180px !important;
    max-height: 300px !important;
    margin-top: 3rem !important;
  }
  
  #login-form-modal-content-form {
    flex: 1 !important;
    min-height: 40vh !important;
    justify-content: center !important;
    padding: 0.8rem !important;
    gap: 0.8rem;
  }
  
  #login-title {
    font-size: 1.8rem;
  }
  
  #login-input, #password-input {
    padding: 0.7rem 0.8rem;
    font-size: 0.85rem;
  }
  
  #login-button {
    max-width: 90%;
    padding: 0.7rem 0;
    font-size: 0.9rem;
  }
  
  .error-message, .success-message {
    font-size: 0.8rem;
    padding: 0.4rem 0.8rem;
  }
}
</style>
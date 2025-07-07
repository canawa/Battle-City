<script setup>
import { ref } from 'vue'

const errorMessage = ref('')
const successMessage = ref('')
const newPassword = ref('')

const resetPasswordProcess = async () => {

  if (newPassword.value.length < 6) {
    errorMessage.value = 'Password must be at least 6 characters long'
    return
  }

  try {
    const response = await fetch('/api/resetpassword', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ newPassword: newPassword.value})
    })
    
    const data = await response.json()
    
    if (data && data.error) {
      errorMessage.value = data.error // принимаем респонс, который мы обозвали data и из него вытаскиваем ошибку
      successMessage.value = ''
    } else if (data && data.detail && data.detail[0] && data.detail[0].type == 'value_error') {
      errorMessage.value = 'Invalid data'
      successMessage.value = ''
    } else {
      successMessage.value = 'Password changed successfully!'
      errorMessage.value = ''
      newPassword.value = ''

    }
  } catch (error) {
    errorMessage.value = 'An error occurred while resetting the password'
    successMessage.value = ''
  }
}
</script>

<template>
<div id="reset-password-modal-container" @click="$emit('closeResetPassword')">
    <div id="reset-password-modal-content" @click.stop>
      <div id="reset-password-modal-content-image">
        <img src="@/assets/forgotPassword.png" alt="reset-password-background" id="battle-city-banner-image">
      </div>
      <div id="reset-password-modal-content-form">
        <h2 id='reset-password-title'>Reset Password</h2>
        
        <input 
          type="password" 
          id="new-password-input" 
          placeholder="Enter new password" 
          v-model="newPassword"
        >
        
        <button id="reset-password-button" @click="resetPasswordProcess()">
          Change Password
        </button>
        
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
        
        <div v-if="successMessage" class="success-message">
          {{ successMessage }}
        </div>
        
        <!-- Дополнительные ссылки -->
        <div class="additional-links">
          <div class="back-to-login">
            <span class="back-text">Вспомнили пароль? </span>
            <a href="#" class="link-text highlighted" @click="$emit('openLogin')">Вернуться к входу</a>
          </div>
        </div>
      </div>
    </div>
</div>
</template>

<style scoped>
#reset-password-modal-content-image {
  width: 25vw;
  height: 100vh;
  display: flex;
  margin: 1rem;
  align-items: center;
}

#reset-password-modal-container {
    position: fixed;
    z-index: 1000;
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(10px);
    background-color: rgba(0, 0, 0, 0.5);
}

#reset-password-modal-content {
  background-color: #121929;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 45vw;
  height: 70vh;
  display: flex;
  flex-direction: row;
  border-radius: 15px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
  color: #0d111b;
  background-color: #121929;
  font-family: 'Manrope', sans-serif;
  font-weight: 600;
  animation: modalSlideIn 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

#battle-city-banner-image {
  display: flex;
  width: 21.5vw;
  border-radius: 15px;
}

@media (max-width: 768px) {
  #battle-city-banner-image {
    content: url('@/assets/forgotPasswordMobile.png');
    width: 100%;
  }
}

#reset-password-modal-content-form {
  width: 30vw;
  height: 70vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  padding: 2rem;
}

#reset-password-title {
  font-size: 2.5rem;
  z-index: 1000 !important;
  font-weight: 700;
  color: white;
  font-family: 'Manrope', sans-serif;
  margin-bottom: 1rem;
  text-align: center;
}

/* Стили для input полей */
#new-password-input {
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

#new-password-input::placeholder {
  color: rgba(255, 255, 255, 0.6);
  font-weight: 400;
}

#new-password-input:focus {
  outline: none;
  border-color: #667eea;
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1), 0 8px 25px rgba(0, 0, 0, 0.2);
  transform: translateY(-2px);
}

#new-password-input:hover {
  border-color: rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.08);
  transform: translateY(-1px);
}

/* Стили для кнопки */
#reset-password-button {
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

#reset-password-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

#reset-password-button:hover::before {
  left: 100%;
}

#reset-password-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
}

#reset-password-button:active {
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

/* Стили для дополнительных ссылок */
.additional-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 300px;
}

.back-to-login {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.back-text {
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

/* Адаптивные стили для мобильных устройств */
@media (max-width: 768px) {
  #reset-password-modal-content {
    width: 85vw !important;
    min-height: 60vh !important;
    max-height: 80vh !important;
    flex-direction: column !important;
    padding: 1rem;
  }
  
  #reset-password-modal-content-image {
    width: 100% !important;
    height: 25vh !important;
    min-height: 200px !important;
    max-height: 300px !important;
    margin: 0 !important;
    margin-top: 2rem !important;
    justify-content: center;
    align-items: center;
  }
  
  #battle-city-banner-image {
    width: 100% !important;
    max-width: 350px !important;
    height: auto !important;
    object-fit: contain !important;
    margin-top: 20rem !important;
  }
  
  #reset-password-modal-content-form {
    width: 100% !important;
    flex: 1 !important;
    min-height: 35vh !important;
    justify-content: center !important;
    padding: 1rem !important;
    gap: 1rem;
  }
  
  #reset-password-title {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    z-index: 1000 !important;
  }
  
  #new-password-input {
    max-width: 90%;
    padding: 0.8rem 1rem;
    font-size: 0.9rem;
  }
  
  #reset-password-button {
    max-width: 90%;
    padding: 0.8rem 0;
    font-size: 1rem;
  }
  
  .additional-links {
    max-width: 100%;
    gap: 0.5rem;
  }
  
  .back-text {
    font-size: 0.8rem;
    z-index: 1000 !important;
  }
  
  .link-text {
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  #battle-city-banner-image {
    content: url('@/assets/forgotPassword.png');
  }
  
  #reset-password-modal-content {
    width: 90vw !important;
    min-height: 70vh !important;
    max-height: 85vh !important;
  }
  
  #reset-password-modal-content-image {
    height: 20vh !important;
    min-height: 150px !important;
    max-height: 250px !important;
    margin-top: 3rem !important;
  }
  
  #reset-password-modal-content-form {
    flex: 1 !important;
    min-height: 40vh !important;
    justify-content: center !important;
    padding: 0.8rem !important;
    gap: 0.8rem;
  }
  
  #reset-password-title {
    font-size: 1.8rem;
    z-index: 1000 !important;
  }
  
  #new-password-input {
    padding: 0.7rem 0.8rem;
    font-size: 0.85rem;
  }
  
  #reset-password-button {
    padding: 0.7rem 0;
    font-size: 0.9rem;
  }
  
  .error-message, .success-message {
    font-size: 0.8rem;
    padding: 0.4rem 0.8rem;
  }
}
</style>
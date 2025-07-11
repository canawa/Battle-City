<script setup>
import { ref } from 'vue'

const voucherCode = ref('')
const message = ref('')
const isLoading = ref(false)





</script>

<template>
  <div class="voucher-modal-overlay" @click="$emit('close')">

    <div class="voucher-modal" @click.stop>
      <div class="voucher-modal-header">
        <h2 class="voucher-title">ACTIVATE VOUCHER</h2>
        <button class="close-button" @click="$emit('close')">×</button>
      </div>
      
      <div class="voucher-modal-content">
        <p class="voucher-description">
          Enter the voucher code to get bonuses or special rewards
        </p>
        
        <input 
          v-model="voucherCode"
          type="text" 
          class="voucher-input" 
          placeholder="Enter the voucher code"
          :disabled="isLoading"
          @keyup.enter="redeemVoucher"
        >
        
        <button 
          class="voucher-button" 
          @click="redeemVoucher"
          :disabled="isLoading || !voucherCode.trim()"
        >
          <span v-if="!isLoading">Activate</span>
          <div v-else class="loading-spinner"></div>
        </button>
        
        <div v-if="message" :class="['message', message.includes('successfully') ? 'success' : 'error']">
          {{ message }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.voucher-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease;
}

.voucher-modal {
  background: linear-gradient(135deg, #1a1f2e 0%, #2d3748 100%);
  border-radius: 20px;
  padding: 2rem;
  width: 90%;
  max-width: 400px;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.1);
  animation: modalSlideIn 0.4s ease;
  position: relative;
  overflow: hidden;
}

.voucher-modal::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
  background-size: 200% 100%;
  animation: shimmer 2s linear infinite;
}

.voucher-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.voucher-title {
  color: white;
  font-size: 1.5rem;
  font-weight: 800;
  font-family: 'Manrope', sans-serif;
  margin: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.close-button {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.6);
  cursor: pointer;
  font-size: 1.5rem;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-button:hover {
  color: white;
  background: rgba(255, 255, 255, 0.1);
  transform: scale(1.1);
}

.voucher-modal-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.voucher-description {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.95rem;
  line-height: 1.5;
  text-align: center;
  margin: 0;
  font-family: 'Manrope', sans-serif;
  font-weight: 400;
}

.voucher-input {
  width: 100%;
  padding: 1rem 1.5rem;
  font-size: 1rem;
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05);
  color: white;
  font-family: 'Manrope', sans-serif;
  font-weight: 500;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
  box-sizing: border-box;
}

.voucher-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
  font-weight: 400;
}

.voucher-input:focus {
  outline: none;
  border-color: #667eea;
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1), 0 8px 25px rgba(0, 0, 0, 0.2);
  transform: translateY(-2px);
}

.voucher-input:hover:not(:focus) {
  border-color: rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.06);
  transform: translateY(-1px);
}

.voucher-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.voucher-button {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-family: 'Manrope', sans-serif;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
}

.voucher-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.voucher-button:hover:not(:disabled)::before {
  left: 100%;
}

.voucher-button:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
}

.voucher-button:active:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.voucher-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.message {
  padding: 0.75rem 1rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  text-align: center;
  font-family: 'Manrope', sans-serif;
  animation: messageSlideIn 0.3s ease;
}

.message.success {
  color: #51cf66;
  background: rgba(81, 207, 102, 0.1);
  border: 1px solid rgba(81, 207, 102, 0.2);
}

.message.error {
  color: #ff6b6b;
  background: rgba(255, 107, 107, 0.1);
  border: 1px solid rgba(255, 107, 107, 0.2);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(-30px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes messageSlideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .voucher-modal {
    width: 95%;
    padding: 1.5rem;
  }
  
  .voucher-title {
    font-size: 1.3rem;
  }
  
  .voucher-description {
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .voucher-modal {
    width: 98%;
    padding: 1.2rem;
  }
  
  .voucher-title {
    font-size: 1.2rem;
  }
  
  .voucher-description {
    font-size: 0.85rem;
  }
}
</style>

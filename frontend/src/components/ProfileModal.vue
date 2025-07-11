<script setup>
import { ref, onMounted } from 'vue'

const emit = defineEmits(['close'])

const userProfile = ref({
  username: '',
  email: '',
  balance: 0,
  registrationDate: '',
  lastLogin: '',
  totalGames: 0,
  wins: 0,
  losses: 0,
  winRate: 0,
  level: 1,
  experience: 0,
  rank: 'Новичок',
  avatar: null,
})

const isLoading = ref(true)
const errorMessage = ref('')

const closeModal = () => {
  emit('close')
}

const fetchUserProfile = async () => {
  try {
    const token = localStorage.getItem('access_token')
    const response = await fetch('/api/userprofile', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    
    if (response.ok) {
      const data = await response.json()
      userProfile.value = {
        ...userProfile.value,
        ...data.user
      }
    } else {
      errorMessage.value = 'Ошибка загрузки профиля'
    }
  } catch (error) {
    console.error('Error fetching user profile:', error)
    errorMessage.value = 'Ошибка соединения'
  } finally {
    isLoading.value = false
  }
}

const updateProfile = async () => {
  // Заготовка для обновления профиля
  console.log('Update profile functionality')
}

const uploadAvatar = async (event) => {
  // Заготовка для загрузки аватара
  const file = event.target.files[0]
  if (file) {
    console.log('Avatar upload:', file.name)
  }
}

onMounted(() => {
  fetchUserProfile()
})
</script>

<template>
  <div id="profile-modal-overlay" @click="closeModal">
    <div id="profile-modal" @click.stop>
      <div id="profile-modal-header">
        <h2>Профиль пользователя</h2>
        <button id="profile-modal-close" @click="closeModal">
          <span class="material-icons">close</span>
        </button>
      </div>

      <div id="profile-modal-content">
        <div v-if="isLoading" id="profile-loading">
          <span class="material-icons">hourglass_empty</span>
          <p>Загрузка профиля...</p>
        </div>

        <div v-else-if="errorMessage" id="profile-error">
          <span class="material-icons">error</span>
          <p>{{ errorMessage }}</p>
        </div>

        <div v-else id="profile-info">
          <!-- Аватар и основная информация -->
          <div id="profile-avatar-section">
            <div id="profile-avatar">
              <img v-if="userProfile.avatar" :src="userProfile.avatar" alt="Avatar">
              <span v-else class="material-icons">account_circle</span>
              <div id="online-indicator" :class="{ 'online': userProfile.isOnline }"></div>
            </div>
            <input type="file" id="avatar-upload" accept="image/*" @change="uploadAvatar" style="display: none;">
            <button id="change-avatar-btn" @click="$refs.avatarUpload.click()">
              <span class="material-icons">photo_camera</span>
              Изменить аватар
            </button>
          </div>

          <!-- Основная информация -->
          <div id="profile-main-info">
            <div class="profile-field">
              <label>Имя пользователя:</label>
              <input type="text" v-model="userProfile.username" placeholder="Введите имя пользователя">
            </div>
            
            <div class="profile-field">
              <label>Email:</label>
              <input type="email" v-model="userProfile.email" placeholder="Введите email">
            </div>

            <div class="profile-field">
              <label>Баланс:</label>
              <div id="profile-balance">
                <span class="material-icons">account_balance_wallet</span>
                {{ userProfile.balance }}$
              </div>
            </div>
          </div>

          <!-- Статистика игр -->
          <div id="profile-stats">
            <h3>Статистика игр</h3>
            <div id="stats-grid">
              <div class="stat-item">
                <span class="stat-label">Всего игр:</span>
                <span class="stat-value">{{ userProfile.totalGames }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Победы:</span>
                <span class="stat-value wins">{{ userProfile.wins }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Поражения:</span>
                <span class="stat-value losses">{{ userProfile.losses }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Процент побед:</span>
                <span class="stat-value">{{ userProfile.winRate }}%</span>
              </div>
            </div>
          </div>

          <!-- Прогресс и достижения -->
          <div id="profile-progress">
            <h3>Прогресс</h3>
            <div class="progress-item">
              <div class="progress-header">
                <span>Уровень {{ userProfile.level }}</span>
                <span>{{ userProfile.experience }} XP</span>
              </div>
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: (userProfile.experience % 100) + '%' }"></div>
              </div>
            </div>
            <div class="rank-info">
              <span class="material-icons">emoji_events</span>
              <span>{{ userProfile.rank }}</span>
            </div>
          </div>

          <!-- Дополнительная информация -->
          <div id="profile-details">
            <h3>Дополнительная информация</h3>
            <div class="detail-item">
              <span class="material-icons">calendar_today</span>
              <span>Дата регистрации: {{ userProfile.registrationDate }}</span>
            </div>
            <div class="detail-item">
              <span class="material-icons">access_time</span>
              <span>Последний вход: {{ userProfile.lastLogin }}</span>
            </div>
          </div>
        </div>
      </div>

      <div id="profile-modal-footer">
        <button id="profile-save-btn" @click="updateProfile">
          <span class="material-icons">save</span>
          Сохранить изменения
        </button>
        <button id="profile-cancel-btn" @click="closeModal">
          Отмена
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
#profile-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

#profile-modal {
  background-color: white;
  border-radius: 1rem;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
}

#profile-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
}

#profile-modal-header h2 {
  margin: 0;
  color: #333;
  font-size: 1.5rem;
}

#profile-modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #666;
  padding: 0.5rem;
  border-radius: 50%;
  transition: background-color 0.3s ease;
}

#profile-modal-close:hover {
  background-color: #f0f0f0;
}

#profile-modal-content {
  padding: 1.5rem;
}

#profile-loading, #profile-error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  color: #666;
}

#profile-loading .material-icons, #profile-error .material-icons {
  font-size: 3rem;
  margin-bottom: 1rem;
}

#profile-avatar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
}

#profile-avatar {
  position: relative;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  margin-bottom: 1rem;
  border: 4px solid #09a24e;
}

#profile-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

#profile-avatar .material-icons {
  font-size: 120px;
  color: #ccc;
}

#online-indicator {
  position: absolute;
  bottom: 10px;
  right: 10px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: #ccc;
  border: 3px solid white;
}

#online-indicator.online {
  background-color: #09a24e;
}

#change-avatar-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background-color: #09a24e;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

#change-avatar-btn:hover {
  background-color: #29ba67;
}

.profile-field {
  margin-bottom: 1rem;
}

.profile-field label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #333;
}

.profile-field input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
  font-size: 1rem;
}

#profile-balance {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  background-color: #f8f9fa;
  border-radius: 0.5rem;
  font-weight: 600;
  color: #09a24e;
}

#profile-stats, #profile-progress, #profile-details {
  margin-top: 2rem;
}

#profile-stats h3, #profile-progress h3, #profile-details h3 {
  margin-bottom: 1rem;
  color: #333;
  border-bottom: 2px solid #09a24e;
  padding-bottom: 0.5rem;
}

#stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.stat-item {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem;
  background-color: #f8f9fa;
  border-radius: 0.5rem;
}

.stat-label {
  color: #666;
}

.stat-value {
  font-weight: 600;
  color: #333;
}

.stat-value.wins {
  color: #09a24e;
}

.stat-value.losses {
  color: #dc3545;
}

.progress-item {
  margin-bottom: 1rem;
}

.progress-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #e0e0e0;
  border-radius: 5px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background-color: #09a24e;
  transition: width 0.3s ease;
}

.rank-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  background-color: #fff3cd;
  border-radius: 0.5rem;
  color: #856404;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0;
  color: #666;
}

#profile-modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  padding: 1.5rem;
  border-top: 1px solid #e0e0e0;
}

#profile-save-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background-color: #09a24e;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

#profile-save-btn:hover {
  background-color: #29ba67;
}

#profile-cancel-btn {
  background-color: #6c757d;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

#profile-cancel-btn:hover {
  background-color: #5a6268;
}

/* Адаптивные стили для мобильных устройств */
@media (max-width: 768px) {
  #profile-modal {
    width: 95%;
    margin: 1rem;
  }
  
  #profile-modal-header {
    padding: 1rem;
  }
  
  #profile-modal-content {
    padding: 1rem;
  }
  
  #profile-modal-footer {
    padding: 1rem;
    flex-direction: column;
  }
  
  #stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  #profile-avatar {
    width: 100px;
    height: 100px;
  }
  
  #profile-avatar .material-icons {
    font-size: 100px;
  }
}

@media (max-width: 480px) {
  #stats-grid {
    grid-template-columns: 1fr;
  }
  
  #profile-modal-header h2 {
    font-size: 1.2rem;
  }
}
</style>

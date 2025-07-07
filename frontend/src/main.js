import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHashHistory } from 'vue-router' // импортнули через npm install vue-router@4
import Header from './components/Header.vue'
import Main from './components/Main.vue'
import Register from './components/RegisterModal.vue'
import Login from './components/LoginModal.vue'
import ResetPasswordModal from './components/ResetPasswordModal.vue'
import LoginModal from './components/LoginModal.vue'

const router = createRouter({
  history: createWebHashHistory(), // стоит понимать что во vue путь /#/resetpassword - это не то же самое что и /resetpassword - тут всегда должен быть #
  routes: [
    { path: '/', component: Main }, // главная страница
    { path: '/resetpassword', component: ResetPasswordModal },
    { path: '/login', component: LoginModal }
  ]
})


const app = createApp(App)
app.use(router)
app.mount('#app') // все что лежит в App.vue будет отображаться в #app (короче js запихивает просто в div с id app)

<script setup> // можно просто писать js код, без экспорта

import Header from './components/Header.vue'

</script>

<template>
<div id="main-container">

  <Header /> <!-- компонент header -->


  <router-view /> <!-- этот тег будет заменяться на компонент, который мы указали в main.js -->
</div>
</template>

<style scoped> /* стили для всего что лежит в App.vue */

#main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
  height: 100vh;
  padding: 0 1%;

}
</style>

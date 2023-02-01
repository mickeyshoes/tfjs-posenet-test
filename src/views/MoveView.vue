<template>
    <div class="home">
      <img alt="Vue logo" src="../assets/yuzLogo.png">
      <HelloWorld msg="Welcome to Your Vue.js App"/>
      <MoveNetComponents></MoveNetComponents>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
import MoveNetComponents from '@/components/MoveNetComponents.vue';

  export default {
    name: 'MoveView',
    components: {
      MoveNetComponents,
    }
  }
  </script>
  
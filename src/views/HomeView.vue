<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/yuzLogo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <PoseNetComponents></PoseNetComponents>
  </div>
</template>

<script>
// @ is an alias to /src
import PoseNetComponents from '@/components/PoseNetComponents.vue';

export default {
  name: 'HomeView',
  components: {
    PoseNetComponents,
  }
}
</script>

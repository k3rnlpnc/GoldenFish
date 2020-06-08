<template>
  <div id="app">
    <div class="site-title">
            <img src="/src/assets/logo.png" class="logo">
            <h1 class="site-name">Golden Fish</h1>
        </div>
        <div class="nav">
            <router-link to="/register" class="button">зарегистрироваться</router-link>
            <router-link to="/login" class="button">войти</router-link>
        </div>
  </div>
</template>

<script>

export default {
  methods: {
    logOut() {
      this.$store.dispatch('auth/logout');
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
</style>

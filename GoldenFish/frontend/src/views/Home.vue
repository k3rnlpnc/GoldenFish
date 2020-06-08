<template>
  <div class="container">
    <div class="site-title">
        <img src="../assets/img/logo.png" class="logo">
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
    name: 'Home',
    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        }
    },
    mounted() {
        document.title = "Главная страница";
        if (this.loggedIn) {
            this.$router.push('/mywishes');
        }
    }
}
</script>

<style scoped>
.site-title {
    position: relative;
    width: 250px;
}

.site-name {
    width: 253px;
    height: 54px;
    font-family: "Ovo";
    font-style: normal;
    font-weight: normal;
    font-size: 48px;
    line-height: 54px;
    color: #D8B661;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.logo {
    position: absolute;
    left: 10px;
    top: -5px;
}

.nav {
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.button {
    color: #FFFFFF;
    font-family: "Poiret One";
    font-style: normal;
    font-weight: normal;
    font-size: 25px;
    line-height: 29px;
    text-decoration: none;
    margin-bottom: 15px;
}
</style>>

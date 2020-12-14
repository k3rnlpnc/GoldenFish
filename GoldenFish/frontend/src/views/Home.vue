<template>
    <div class="container">
        <div class="site-title">
            <img src="../assets/img/logo.png" class="logo">
            <h1 class="site-name">Golden Fish</h1>
            <img src="../assets/img/christmas-decoration.png" class="cristmas-decoration">
        </div>
        <div class="nav">
            <router-link to="/register" class="button">зарегистрироваться</router-link>
            <router-link to="/login" class="button">войти</router-link>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Home'
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
    margin: 0;
}

.logo {
    position: absolute;
    left: 10px;
    top: -36px;
}

.cristmas-decoration {
    width: 250px;
    
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
</style>

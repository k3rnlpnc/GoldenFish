<template>
    <header class="app-header">
        <img src="../assets/img/logo.png" class="logo">
        <form>
            <input name="username" placeholder="Поиск..." class="search-bar" autocomplete="off">
            <a href="#" class="magnifer-button"><img src="../assets/img/magnifer.png"></a>
        </form>
        <div class="dropdown">
            <div class="dropdown-link">
                <span class="dropdow-username">Username</span>
                <img src="images/dropdown.png">
            </div>
            <div class="dropdown-content">
                <router-link to="/profile">Профиль</router-link>
                <a @click="logout">Выйти</a>
            </div>
            </div>
    </header>
</template>

<script>
import AuthService from '../services/auth.service';

export default {
    methods: {
        logout() {
            AuthService.logout();
        }
    }
}
</script>

<style scoped>
header {
    font-family: "Poiret One";
    background: #6C3F5E;
    min-width: 100%;
    height: 52px;
    display: flex;
    justify-content: space-between;
    overflow: hidden;
}

header .logo {
    width: 83px;
    height: 51px;
    margin-left: 9px;
}

header form .search-bar {
    margin-top: 17px;
    font-family: Poiret One;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 23px;
    background: #6C3F5E;
    width: 388px;
    border: 0;
    border-bottom: 1px solid #C6A960;
    color: #C6A960;
}

header form .search-bar::-webkit-input-placeholder { 
    font-family: Poiret One;
    color: #C6A960;
    padding: 4px;
}

header form .magnifer-button img {
    width: 22px;
    height: 22px;
}

header .dropdown {
    font-size: 23px;
    line-height: 27px;
    margin-top: 16px;
    margin-right: 62px;
    color: #C6A960;
}

header .dropdown .dropdown-link img {
    width: 13px;
    height: 11px;
}

.dropdown:hover .dropdown-content {
    display: block;
}

header .dropdown .dropdown-content {
    margin-top: 9px;
    display: none;
    position: absolute;
    background: #C6A960;
    z-index: 1;
}

header .dropdown .dropdown-content a {
    width: 125px;
    height: 28px;
    text-decoration: none;
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.5);
    font-size: 18px;
    line-height: 21px;
    display: block
}
</style>
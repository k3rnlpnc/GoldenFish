<template>
    <header class="app-header">
        <img src="../assets/img/logo.png" class="logo">
        <div class="search">
            <input v-model="friendName" placeholder="Поиск..." class="search-bar" autocomplete="off">
            <a @click="findFriend" class="magnifer-button">
                <img src="../assets/img/magnifer.png">
            </a>
        </div>
        <div class="dropdown">
            <div class="dropdown-link">
                <span v-if="username" class="dropdow-username">{{username}}</span>
                <span v-else class="dropdow-username">Username</span>
                <img src="../assets/img/dropdown.png">
            </div>
            <div class="dropdown-content">
                <router-link to="/profile">Профиль</router-link>
                <a @click="logout">Выйти</a>
            </div>
        </div>
    </header>
</template>

<script>
import UserService from '../services/user.service';
import User from '../models/user';

export default {
    data() {
        return {
            username: '',
            friendName: ''
        }
    },
    mounted() {
        let user = new User();
        UserService.getProfileInfo().then(
            response => {
                user = response.data;
                this.username = user.username;
            }
        );
    },
    methods: {
        findFriend() {
            try {
                this.$metrika.reachGoal('findFriend');
            } catch (e) {
                console.log(e);
            }
            this.$router.push('/friends_search/' + this.friendName);
            this.friendName = '';
        },
        logout() {
            this.$store.dispatch('auth/logout');
            this.$router.push('/home');
        }
    }
}
</script>

<style scoped>
header {
    font-family: "Poiret One";
    background: #6C3F5E;
    width: 100%;
    min-width: 900px;
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

header .search .search-bar {
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

header .search .search-bar::-webkit-input-placeholder { 
    font-family: Poiret One;
    color: #C6A960;
    padding: 4px;
}

header .search .magnifer-button {
    background: #6C3F5E;
    border: 0;
    cursor: pointer;
}

header .search .magnifer-button img {
    width: 22px;
    height: 22px;
}

header .dropdown {
    font-size: 23px;
    line-height: 27px;
    margin-top: 16px;
    margin-right: 62px;
    color: #C6A960;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.dropdown-link img {
    width: 13px;
    height: 11px;
    padding-left: 5px;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown-content {
    display: none;
    position: absolute;
    top: 52px;
    background: #C6A960;
    z-index: 1;
}

.dropdown-content a {
    color: #592549;
    cursor: pointer;
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
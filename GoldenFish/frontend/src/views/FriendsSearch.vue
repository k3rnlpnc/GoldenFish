<template>
    <div class="container">
        <h3 class="search-title">Результат поиска</h3>
        <div class="message">{{message}}</div>
        <div v-if="users.length > 0" class="result">
            <div 
                class="add-friend"
                v-for="user in users"
                :key="user.id"
            >
                <div class="user-info">
                    <span v-if="user.username" class="username">{{user.username}}</span>
                    <span v-if="user.name && user.username" class="fullname">
                        {{user.name}} {{user.surname}}
                    </span>
                </div>
                <div class="add-friend-button">
                    <button @click="addFriend(user.id)">
                        <img src="../assets/img/checkmark.png">
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import UserService from '../services/user.service';
import FriendService from '../services/friend.service';

export default {
    data() {
        return {
            message: '',
            users: []
        };
    },
    computed: {
        username() {
            return this.$route.params.username;
        }
    },
    watch: {
        username: function () {
            UserService.findFriendByUsername(this.username).then(
            response => {
                this.users = response.data;
                if(response.data.length === 0)
                    this.message = 'Поиск не дал результатов';
            },
            error => {
                this.message = 'Неизвестная ошибка';
                console.log(error);
            }
        );
        }
    },
    mounted() {
        document.title = "Поиск друзей";
    },
    methods: {
        addFriend(id) {
            FriendService.addFriend(id).then(
                () => {
                    this.message = 'Заявка в друзья отправлена';
                }
            );
        }
    }
}
</script>

<style scoped>
.search-title {
    text-align: center;
    margin: 80px 80px 40px 80px;
    font-size: 30px;
    line-height: 35px;
    color: #6C3F5E;
}

.message {
    font-size: 23px;
    text-align: center;
    font-weight: bold;
}

.result {
    display: flex;
    flex-wrap: wrap;
    margin: 0 30px;
}

.add-friend {
    padding: 15px;
    display: flex;
    flex-direction: row;
}

.user-info {
    background: #ECE3E3;
    height: 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px 20px;
}

.user-info .username {
    font-size: 25px;;
}

.user-info .fullname {
    font-size: 20px;
}

.add-friend-button {
    background: #ECE3E3;
    margin-left: 2px;
    display: flex;
    align-items: center;
}

.add-friend-button button {
    background: inherit;
    border: 0;
}

.add-friend-button button img {
    width: 18px;
    height: 18px;
    cursor: pointer;
}
</style>
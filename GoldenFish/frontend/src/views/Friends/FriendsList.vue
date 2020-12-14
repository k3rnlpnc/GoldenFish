<template>
    <div>
        <spinner v-if="loading" class="spinner"></spinner>
        <div v-else class="content">
            <div v-if="friends.length > 0" class="friends-list">
                <div 
                    class="friend-line" 
                    v-for="(friend, index) in friends" 
                    :key="friend.id"
                >
                    <div class="friend-info" @click="onFriendProfile(friend.id)">
                        <span class="username" v-if="friend.username">{{friend.username}}</span>
                        <span
                            class="fullname" 
                            v-if="friend.name && friend.surname"
                        >
                        {{friend.name}} {{friend.surname}}
                        </span>
                    </div>
                    <div class="delete-friend-button">
                        <button 
                            @click="deleteFriend(friend.id, index)"
                            name="delete-friend"
                        >
                            <img src="../../assets/img/delete.png">
                        </button>
                    </div>
                </div>
            </div>
            <div v-else class="no-friends">Список друзей пуст</div>
        </div>
    </div>
</template>

<script>
import Swal from 'sweetalert2/src/sweetalert2.js'
import FriendService from '../../services/friend.service';
import Spinner from '../Spinner'

export default {
    data() {
        return {
            loading: true,
            friends: []
        };
    },
    components: 
    {
        Spinner
    },
    mounted() {
        document.title = "Друзья";
        this.getFriends();
    },
    methods: {
        getFriends() {
            FriendService.getFriends().then(
                response => {
                    this.friends = response.data;
                    this.loading = false;
                },
                error => {
                    let message = (error.response && error.response.data) ||
                        error.message ||
                        error.toString();
                    console.log(message);
                }
            );
        },
        deleteFriend(id, index) {
            Swal.mixin({
                customClass: {
                    confirmButton: 'confirm-button',
                    cancelButton: 'confirm-button',
                },
                    buttonsStyling: false
            }).fire({
                background: '#E7E1E1',
                html: '<span class="confirm-text">Вы действительно хотите удалить друга?</span>',
                showCancelButton: true,
                confirmButtonText: 'Удалить',
                cancelButtonText: 'Отменить'
            }).then((result) => {
                if (result.value)
                    FriendService.deleteFriend(id).then(
                        () => {
                            this.friends.splice(index, 1);
                        }
                    );
            })
        },
        onFriendProfile(id) {
            this.$router.push('/friend/' + id);
        }
    }
}
</script>

<style scoped>
.spinner {
    margin: 30vh auto;
}

.no-friends {
    font-size: 23px;
    text-align: center;
    font-weight: bold;
}

.friends-list {
    display: flex;
    justify-content: start;
    flex-wrap: wrap;
    margin: 0 30px;
}

.friend-line {
    padding: 15px;
    display: flex;
    flex-direction: row;
    cursor: pointer;
}

.friend-info {
    background: #ECE3E3;
    height: 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px 20px;
}

.friend-info .username {
    font-size: 25px;;
}

.friend-info .fullname {
    font-size: 20px;
}

.delete-friend-button {
    background: #ECE3E3;
    margin-left: 2px;
    display: flex;
    align-items: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.delete-friend-button button{
    background: inherit;
    border: 0;
}

.delete-friend-button button img{
    width: 18px;
    cursor: pointer;
    padding-top: 5px;
}
</style>

<style>
.confirm-text {
    font-family: "Poiret One";
    font-size: 20px;
    font-weight: bold;
}

.confirm-button {
    background: #E7E1E1;
    border: 0;
    cursor: pointer;
    font-size: 18px;
    font-family: Poiret One;
    margin: 20px;
}

.confirm-button:hover {
    font-weight: bold;
}
</style>
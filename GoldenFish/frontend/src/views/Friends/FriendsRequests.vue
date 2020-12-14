<template>
    <div>
        <spinner v-if="loading" class="spinner"></spinner>
        <div v-else class="content">
            <div v-if="requests.length > 0" class="friends-request-list">
                <div 
                    class="friends-request-line"
                    v-for="(request, index) in requests" 
                    :key="request.id"
                >
                    <div class="friend-info">
                        <span v-if="request.username" class="username">{{request.username}}</span>
                        <span v-if="request.name && request.surname" class="fullname">
                            {{request.name}} {{request.surname}}
                        </span>
                    </div>
                    <div class="request-buttons">
                        <button @click="acceptRequest(request.id, index)">
                            <img src="../../assets/img/checkmark.png">
                        </button>
                        <button @click="rejectRequest(request.id, index)">
                            <img src="../../assets/img/delete.png">
                        </button>
                    </div>
                </div>
            </div>
            <div v-else class="no-requests">Заявок в друзья нет</div>
        </div>
    </div>
</template>

<script>
import FriendService from '../../services/friend.service';
import Spinner from '../Spinner'

export default {
    data() {
        return {
            loading: true,
            requests: []
        };
    },
    components: {
        Spinner
    },
    mounted() {
        document.title = "Заявки в друзья";
        FriendService.getFriendRequests().then(
            response => {
                this.requests = response.data;
                this.loading = false;
            }
        );
    },
    methods: {
        acceptRequest(id, index) {
            FriendService.acceptRequest(id).then(
                () => {
                    this.requests.splice(index, 1);
                }
            );
        },
        rejectRequest(id, index) {
            FriendService.rejectRequest(id).then(
                () => {
                    this.requests.splice(index, 1);
                }
            );
        }
    }
}
</script>

<style scoped>
.spinner {
    margin: 30vh auto;
}

.friends-request-list {
    display: flex;
    justify-content: start;
    flex-wrap: wrap;
    margin: 0 30px;
}

.friends-request-line {
    padding: 15px;
    display: flex;
    flex-direction: row;
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

.request-buttons {
    background: #ECE3E3;
    margin-left: 2px;
    display: flex;
    align-items: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.request-buttons button {
    background: inherit;
    border: 0;
}

.request-buttons button img {
    width: 18px;
    cursor: pointer;
    padding-top: 5px;
}
.no-requests {
    font-size: 23px;
    text-align: center;
    font-weight: bold;
}
</style>
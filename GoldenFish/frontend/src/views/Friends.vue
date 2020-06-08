<template>
    <div class="content">
        <div class="tabs">
            <div to="/friends_list" v-bind:class="{ active: isFriendsList }" class="friends-request-tab" @click="onFriendsList">Друзья</div>
            <div to="/friends_requests" v-bind:class="{ active: isFriendsRequests }" class="friends-request-tab" @click="onFriendsRequests">Заявки</div>
        </div>
        <component :is="layout">
            <router-view/>
        </component>
    </div>
</template>

<script>

export default {
    data() {
        return {
            isFriendsList: true,
            isFriendsRequests: false
        };
    },
    computed: {
        currentUser() {
            return this.$store.state.auth.user;
        },
        layout() {
            if(this.isFriendsList)
                return 'friends-list';
            else
                return 'friends-requests';
        }
    },
    methods: {
        onFriendsList() {
            this.isFriendsList = true;
            this.isFriendsRequests = false;
        },
        onFriendsRequests() {
            this.isFriendsList = false;
            this.isFriendsRequests = true;
        }
    }
}
</script>

<style scoped>
.tabs {
    display: flex;
    justify-content: center;
    margin: 35px;
}

.friends-tab, .friends-request-tab {
    font-size: 23px;
    width: 160px;
    height: 30px;
    display: flex;
    justify-content: center;
    cursor: pointer;
    padding: 3px;
    background: rgba(198, 169, 96, 0.6);
}

.active {
    background: #C6A960;
}
</style>
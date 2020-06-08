<template>
    <div class="content">
        <div class="user-info">
            <span v-if="user.name" class="username">{{user.name}}</span>
            <span v-if="user.birthday" class="user-birthday">{{getRusFormatDate(user.birthday)}}</span>
        </div>
        <div v-if="wishes.length > 0" class="wishes">
            <div 
                class="wish-line" 
                v-for="wish in wishes" 
                :key="wish.id" 
            >
                <div class="wish-info" @click="openModal(wish.id)">
                    <div class="wish-info-line">
                        <span v-if="wish.name" class="wish-name">{{wish.name}}</span>
                        <span v-if="wish.giver_username" class="friend-name">{{wish.giver_username}}</span>
                    </div>
                </div>
                <div class="wish-buttons">
                    <a disabled v-if="wish.giver_username"><img src="../assets/img/grey-gift.png"></a>
                    <a v-else @click="addToGifts(wish.id)"><img src="../assets/img/gift.png"></a>
                </div>
            </div>
        </div>
        <div v-else class="message">Пользователь пока не добавил желания</div>
        <wish-info-modal
            v-if="showModal" 
            :id="idForModal"
            @close="showModal = false"
        >
        </wish-info-modal>
    </div>
</template>

<script>
import User from '../models/user';
import WishInfoModal from './WishInfoModal'
import FriendService from '../services/friend.service';
import UserService from '../services/user.service'
import GiftService from '../services/gift.service'

export default {
    data() {
        return {
            id: null,
            user: new User(),
            wishes: [],
            showModal: false,
            myUsername: 'username',
            idForModal: 0
        };
    },
    components: {
        WishInfoModal
    },
    mounted() {
        this.id = this.$route.params.id;
        if(this.id) {
            UserService.getUserInfo(this.id).then(
                response => {
                    this.user = response.data;
                }
            ); 
        }
        UserService.getProfileInfo().then(
            response => {
                const me = response.data;
                this.myUsername = me.username;
            }
        ) 
        this.getWishes();
    },
    methods: {
        getRusFormatDate(date) {
            let arr = date.split('-');
            return arr[2] + '.' + arr[1] + '.' + arr[0];
        },
        addToGifts(wish_id) {
            GiftService.addGift(this.id, wish_id).then(
                () => {
                    this.getWishes();
                },
                error => {
                    console.log(error);
                }
            );
        },
        openModal(id) {
            this.idForModal = id;
            this.showModal = true;
        },
        getWishes() {
            FriendService.getFriendWishes(this.id).then(
                response => {
                    this.wishes = response.data;
                }
            );
        }
    }
}
</script>

<style scoped>
.content {
    font-family: "Poiret One";
}

.message {
    font-size: 23px;
    text-align: center;
    font-weight: bold;
}

.user-info {
    display: flex;
    justify-content: space-between;
    margin: 60px;
    margin-bottom: 40px;
    font-weight: 500;
    color:#592549;;
}

.user-info .username {
    font-size: 32px;
    line-height: 32px;
}

.user-info .user-birthday {
    font-size: 23px;
    line-height: 23px;
}

.wishes {
    margin: 0px 50px;
}

.wish-line {
    width: inherit;
    height: 40px;
    display: flex;
    margin-bottom: 10px;
    cursor: pointer;
}

.wish-info {
    background: #ECE3E3;
    width: 100%;
    font-size: 20px;
    line-height: 20px;
    color: #000000;
    padding: 10px 25px;
}

.wish-info-line {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #E1DADA;
}

.wish-buttons {
    background: rgb(198, 169, 96);
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-left: 6px;
}

.wish-buttons a img {
    height: 18px;
    width: 22px;
    padding: 0px 5px;
    cursor: pointer;
}
</style>
<template>
    <div>
        <spinner v-if="loading" class="spinner"></spinner>
        <div v-else class="container">
            <div v-if="wishes.length > 0" class="wishes">
                <div v-for="wish in wishes" :key="wish.id" class="wish-line" @click="openModal(wish.id)">
                    <div class="wish-info">
                        <div class="wish-info-line">
                            <span class="wish-name" v-if="wish.name">{{wish.name}}</span>
                            <span 
                                class="friend-name" 
                                v-if="wish.giver_id">{{getFriendUsername(wish.giver_id)}}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="no-wishes">Исполненных желаний пока нет...</div>
            <wish-info-modal
                v-if="showModal" 
                :id="idForModal"
                @close="showModal = false"
            >
            </wish-info-modal>
        </div>
    </div>
</template>

<script>
import DreamService from '../../services/dream.service';
import UserService from '../../services/user.service';
import WishInfoModal from './WishInfoModal'
import Spinner from '../Spinner'

export default {
    data() {
        return {
            loading: true,
            wishes: [],
            showModal: false,
            idForModal: 0
        };
    },
    components: {
        WishInfoModal, Spinner
    },
    mounted() {
        document.title = "Исполненные желания";
        DreamService.getFulfilledWishes().then(
            response => {
                this.wishes = response.data;
                this.loading = false;
            }
        );
    },
    methods: {
        getFriendUsername(id) {
            let friend;
            UserService.getUserInfo(id).then(
                response => {
                    friend = response.data;
                }
            );
            return friend.username;
        },
        openModal(id) {
            this.idForModal = id;
            this.showModal = true;
        }
    }
}
</script>

<style scoped>
.container {
    font-family: "Poiret One";
}
.wishes {
    margin: 50px;
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
.no-wishes {
    margin: 50px;
    text-align: center;
    font-size: 23px;
    font-weight: bold;
    color: #000000;
}
</style>
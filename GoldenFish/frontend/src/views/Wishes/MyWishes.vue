<template>
    <div>
        <spinner v-if="loading" class="spinner"></spinner>
        <div v-else class="content">
            <div class="user-info">
                <span v-if="user.name" class="username">{{user.username}}</span>
                <span v-if="user.birthday" class="user-birthday">{{getRusFormatDate(user.birthday)}}</span>
            </div>
            <div v-if="wishes.length > 0" class="wishes">
                <div v-for="(wish, index) in wishes" :key="wish.id" class="wish-line">
                    <div class="wish-info" @click="openEditModal(wish.id)">
                        <div class="wish-info-line">
                            <span v-if="wish.name" class="wish-name">{{wish.name}}</span>
                            <span v-if="wish.giver_username" class="friend-name">Подарок занят</span>
                        </div>
                    </div>
                    <div class="wish-buttons">
                        <a @click="deleteWish(wish.id, index)"><img src="../../assets/img/delete.png"></a>
                        <a @click="setWishFulfilled(wish.id, index)"><img src="../../assets/img/checkmark.png"></a>
                    </div>
                </div>
                <wish-modal 
                    v-if="showEditModal" 
                    :id="wishIdForModal"
                    @close="closeModalWindow"
                    @save="editWish"
                >
                </wish-modal>
            </div>
            <div v-else class="add-wish-title">Добавьте желание</div>
            <div class="add-wish">
                <button class="add-wish-button" @click="openAddModal"><img src="../../assets/img/plus.png"></button>
            </div>
            <wish-modal 
                v-if="showAddModal" 
                id=""
                @close="closeModalWindow"
                @save="addWish"
            >
            </wish-modal>
        </div>
    </div>
</template>

<script>
import Swal from 'sweetalert2/src/sweetalert2.js'
import User from '../../models/user';
import UserService from '../../services/user.service';
import DreamService from '../../services/dream.service';
import WishModal from './WishModal'
import Spinner from '../Spinner'

export default {
    name: 'MyWishes',
    data() {
        return {
            loading: true,
            user: new User(),
            wishes: [],
            showEditModal: false,
            showAddModal: false,
            wishIdForModal: '',
            closeModal: 0
        };
    },
    components: {
        WishModal, Spinner
    },
    mounted() {
        document.title = "Мои желания";
        UserService.getProfileInfo().then(
            response => {
                this.user = response.data;
            }
        ); 
        this.getMyWishes();  
    },
    methods: {
        getRusFormatDate(date) {
            let arr = date.split('-');
            return arr[2] + '.' + arr[1] + '.' + arr[0];
        },
        openEditModal(id) {
            this.wishIdForModal = id;
            this.showEditModal = true;
        },
        openAddModal() {
            try {
                this.$metrika.reachGoal('addWish');
            } catch (e) {
                console.log(e);
            } 
            this.showAddModal = true;
        },
        closeModalWindow() {
            this.showAddModal = false;
            this.showEditModal = false;
            this.getMyWishes();     
        },
        addWish(data) {
            DreamService.addWish(data).then(
                () => {
                    this.loading = true;
                    this.getMyWishes().then(
                        () => {
                            this.loading = false;
                        }
                    );
                }
            );
            this.showAddModal = false;
        },
        editWish(data) {
            DreamService.editWish(data).then(
                () => {
                    this.loading = true;
                    this.getMyWishes().then(
                        () => {
                            this.loading = false;
                        }
                    );
                }
            );
            this.showEditModal = false;
        },
        deleteWish(id, index) {
            Swal.mixin({
                customClass: {
                    confirmButton: 'confirm-button',
                    cancelButton: 'confirm-button',
                },
                    buttonsStyling: false
            }).fire({
                background: '#E7E1E1',
                html: '<span class="confirm-text">Вы действительно хотите удалить желание?</span>',
                showCancelButton: true,
                confirmButtonText: 'Удалить',
                cancelButtonText: 'Отменить'
            }).then((result) => {
                if (result.value) {
                    DreamService.deleteWish(id).then(
                        () => {
                            this.wishes.splice(index, 1); 
                        }
                    );
                }
            })
        },
        setWishFulfilled(id, index) {
            Swal.mixin({
                customClass: {
                    confirmButton: 'confirm-button',
                    cancelButton: 'confirm-button',
                },
                    buttonsStyling: false
            }).fire({
                background: '#E7E1E1',
                html: '<span class="confirm-text">Вы действительно хотите добавить желание в список исполненных?</span>',
                showCancelButton: true,
                confirmButtonText: 'Добавить',
                cancelButtonText: 'Отменить'
            }).then((result) => {
                if (result.value) {
                    DreamService.setWishFulfilled(id).then(
                        () => {
                            this.wishes.splice(index, 1); 
                        }
                    );
                }
            })
        },
        getMyWishes() {
            DreamService.getMyWishes().then(
                response => {
                    this.wishes = response.data;
                    this.loading = false;
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
    align-items: center;
    justify-content: space-around;
}

.wish-buttons a img {
    height: 12px;
    width: 17px;
    padding: 0px 7px;
    cursor: pointer;
}

.add-wish {
    padding: 20px;
    display: flex;
    justify-content: center;
}

.add-wish-title {
    font-size: 23px;
    text-align: center;
}

.add-wish-button {
    background: inherit;
    border: 0;
    cursor: pointer;
}

.add-wish-button img {
    width: 25px;
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
<template>
    <div class="container">
        <spinner v-if="loading" class="spinner"></spinner>
        <div v-else class="content">
            <div v-if="gifts.length > 0" class="wishes">
                <div 
                    class="wish-line" 
                    v-for="(gift, index) in gifts"
                    :key="gift.id"
                >
                    <div class="wish-info" @click="openModal(gift.id)">
                        <div class="wish-info-line">
                            <span v-if="gift.name" class="wish-name">{{gift.name}}</span>
                        </div>
                    </div>
                    <div class="wish-buttons">
                        <a @click="deleteGift(gift.id, index)"><img src="../../assets/img/delete.png"></a>
                    </div>
                </div>
            </div>
            <div v-else class="message">В вашем списке нет запланированных подарков</div>
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
import Swal from 'sweetalert2/src/sweetalert2.js'
import GiftService from '../../services/gift.service'
import WishInfoModal from '../Wishes/WishInfoModal'
import Spinner from '../Spinner'

export default {
    data() {
        return {
            gifts: [],
            showModal: false,
            idForModal: 0,
            loading: true
        };
    },
    components: {
        WishInfoModal, Spinner
    },
    mounted() {
        document.title = "Хочу подарить";
        GiftService.getGifts().then(
            response => {
                this.gifts = response.data;
                this.loading = false;
            }
        );
    },
    methods: {
        openModal(id) {
            this.idForModal = id;
            this.showModal = true;
        },
        deleteGift(id, index) {
            Swal.mixin({
                customClass: {
                    confirmButton: 'confirm-button',
                    cancelButton: 'confirm-button',
                },
                    buttonsStyling: false
            }).fire({
                background: '#E7E1E1',
                html: '<span class="confirm-text">Вы действительно хотите удалить подарок из списка "Хочу подарить"?</span>',
                showCancelButton: true,
                confirmButtonText: 'Удалить',
                cancelButtonText: 'Отменить'
            }).then((result) => {
                if (result.value) {
                    GiftService.deleteGift(id).then(
                        () => {
                            this.gifts.splice(index, 1);
                        }
                    );
                }
            })
        }
    }
}
</script>

<style scoped>
.container {
    font-family: "Poiret One";
}

.wishes {
    margin: 0px 50px;
    margin-top: 50px;
}

.wish-line {
    width: inherit;
    height: 40px;
    display: flex;
    margin-bottom: 15px;
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
    cursor: pointer;
}

.wish-buttons {
    background: rgb(198, 169, 96);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-left: 6px;
}

.wish-buttons a img {
    height: 12px;
    width: 17px;
    padding: 0px 5px;
    cursor: pointer;
}

.message {
    margin: 50px;
    text-align: center;
    font-size: 23px;
    font-weight: bold;
    color: #000000;
}
</style>
<template>
    <div class="container">
        <div class="modal-mask">
            <div class="modal-content">
                <form class="modal-form" name="form" @submit="saveWish">
                    <input
                        v-model="wish.name"
                        name="name"
                        autocomplete="off"
                        class="wish-name"
                        placeholder="Название..."
                    />
                    <div class="optional-data-block">
                        <div class="description-store-link-block">
                            <textarea
                                v-model="wish.description"
                                placeholder="Добавить описание..."
                                name="description"
                                autocomplete="off"
                                class="optional-data description"
                            />
                            <input
                                v-model="wish.store_link"
                                placeholder="Добавить ссылку на магазин..."
                                name="store-link"
                                autocomplete="off"
                                class="optional-data store-link"
                            />
                        </div>
                        <div class="img-block">
                            <img
                                v-if="wish.image_link"
                                :src="wish.image_link"
                                class="optional-data image"
                                alt="Изображение"
                            >
                            <input
                                v-model="wish.image_link"
                                placeholder="Добавить ссылку на изображение..."
                                name="image-link"
                                autocomplete="off"
                                class="optional-data image-link"
                            />
                        </div>
                    </div>
                    <div class="buttons">
                        <button @click="$emit('close')">Назад</button>
                        <button :disabled="!wish.name" type="submit">Сохранить</button>
                    </div> 
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import DreamService from '../services/dream.service';
import Dream from '../models/dream';

export default {
    name: 'WishModal',
    props: ['id'],
    data() {
        return {
            wish: new Dream()
        };
    },
    mounted() {
        if(this.id) {
            DreamService.getWishInfo(this.id).then(
                response => {
                    this.wish = response.data;
                }
            );
        }
    },
    methods: {
        saveWish() {
            if(!this.id) {
                DreamService.addWish(this.wish);
            }
            else {
                DreamService.editWish(this.wish);
            }
            this.$emit('close');
        }
    }
}
</script>

<style scoped>
.modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal-content {
    background: #E7E1E1;
    border-radius: 5px;
    width: 50%;
    padding: 25px;
    font-family: "Poiret One";
}

.modal-form {
    display: flex;
    flex-direction: column;
}

.wish-name {
    background: inherit;
    border: 0;
    border-bottom: 1px solid rgba(198, 169, 96, 0.5);
    margin-bottom: 12px;
    padding-left: 20px;
}

.optional-data-block {
    display: flex;
}

.wish-name::-webkit-input-placeholder, .wish-name { 
    font-size: 23px;
    color: black; 
    font-family: "Poiret One";
}

.description-store-link-block, .img-block {
    display: flex;
    flex-direction: column;
    width: 50%;
}

.optional-data {
    margin: 5px;
    border: 0;
    resize: none;
    background: rgba(197, 167, 89, 0.3);  
    padding: 10px 20px;
}

.optional-data::-webkit-input-placeholder, .optional-data {
    font-family: "Poiret One";
    font-size: 17px;
    color: black;
}

.description{
    height: 150px;
}

.image {
    padding: 0;
    overflow:scroll;
    max-height: 50vh;
}

.store-link, .image-link {
    height: 30px;
}

.modal-form .buttons {
    display: flex;
    justify-content: center;
}

.modal-form .buttons button {
    background: inherit;
    border: 0;
    cursor: pointer;
    font-size: 18px;
    font-family: Poiret One;
    margin: 20px;
}
button:disabled {
    color: black;
    cursor: not-allowed !important;
}
</style>
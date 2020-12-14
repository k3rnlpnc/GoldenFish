<template>
    <div class="container" v-if="!loading">
        <div class="modal-mask">
            <div class="modal-content">
                <div class="name" v-if="wish.name">{{wish.name}}</div>
                <div class="description optional-data" v-if="wish.description">{{wish.description}}</div>
                <a 
                    class="store-link optional-data" 
                    v-if="wish.store_link" 
                    :href="wish.store_link"
                    target="_blank"
                >
                    Ссылка на магазин
                </a>
                <div class="img-container optional-data">
                    <img class="image" v-if="wish.image_link" alt="Изображение" :src="wish.image_link">
                </div>
                <div class="buttons">
                    <button @click="$emit('close')">Назад</button>
                </div> 
            </div>
        </div>
    </div>
</template>

<script>
import DreamService from '../../services/dream.service';
import Dream from '../../models/dream';

export default {
    name: 'WishModal',
    props: ['id'],
    data() {
        return {
            loading: true,
            wish: new Dream()
        };
    },
    mounted() {
        if(this.id) {
            DreamService.getFriendWish(this.id).then(
                response => {
                    this.wish = response.data;
                    this.loading = false;
                }
            );
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
    justify-content: center;
    align-items: center;
}

.modal-content {
    background: #E7E1E1;
    width: 50%;
    padding: 25px;
    font-family: "Poiret One";
    display: flex;
    flex-direction: column;
    max-height: 80vh;
    overflow-y: scroll;
}

.modal-content * {
    margin-bottom: 10px;
}

.name {
    border-bottom: 1px solid rgba(198, 169, 96, 0.5);
    padding-left: 20px;
    font-size: 23px;
}

.description {
    background: rgba(197, 167, 89, 0.3);  
    padding: 10px 20px;
    font-size: 20px;
}

.store-link {
    font-size: 20px;
    color: black;
    text-decoration: none;
}

.store-link:hover {
    text-decoration: underline;
}

.img-container {
    max-height: 50%;
    max-width: inherit;
    display: flex;
    justify-content: center;
}

.image {
    background-size: 100% auto;
    max-width: 100%;
}

.buttons {
    display: flex;
    justify-content: center;
}

.buttons button {
    background: inherit;
    border: 0;
    cursor: pointer;
    font-size: 18px;
    font-family: Poiret One;
    margin: 10px;
    margin-bottom: 10px;
}
</style>
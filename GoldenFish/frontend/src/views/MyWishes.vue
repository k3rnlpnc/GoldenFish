<template>
    <div class="content">
        <div class="user-info">
            <span v-if="user.username" class="username">{{user.username}}}</span>
            <span v-if="user.birthday" class="user-birthday">{{user.birthday}}</span>
        </div>
        <div class="wishes">
            <div class="wish-line">
                <div class="wish-info">
                    <div class="wish-info-line">
                        <span class="wish-name"></span>
                        <span class="friend-name"></span>
                    </div>
                </div>
                <div class="wish-buttons">
                    <a><img src="../assets/img/delete.png"></a>
                    <a><img src="../assets/img/checkmark.png"></a>
                </div>
            </div>
        </div>
        <div class="add-wish">
            <a href="#" class="add-wish-button"><img src="../assets/img/plus.png"></a>
        </div>
    </div>
</template>

<script>

export default {
    name: 'MyWishes',
    data() {
        return {
        user: this.$store.currentUser,
        wishes: [
                {
                    name: 'Велосипед',
                    giver: 'rediska'
                }, 
                {
                    name: 'Машина',
                    giver: null
                }
            ]
        };
    },
    computed: {
        currentUser() {
            return this.$store.state.auth.user;
        }
    },
    methods: {
        addWish() {

        }
    }
}
</script>

<style scoped>
.content {
    font-family: "Poiret-One";
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
    margin-left: 6px;
}

.wish-buttons a img {
    height: 12px;
    width: 17px;
    padding: 0px 5px;
    cursor: pointer;
}

.add-wish {
    width: 100%;
    padding: 20px;
    display: flex;
    justify-content: center;
}

.add-wish-button img {
    width: 25px;
}
</style>
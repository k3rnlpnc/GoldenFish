<template>
    <menu class="app-menu">
        <menu>
            <router-link to="/friends">
                <li v-bind:class="{ 'selected-menu-item' : isFriendsChecked }">
                    Друзья
                </li>
            </router-link>

            <router-link to="/mywishes">
                <li v-bind:class="{ 'selected-menu-item' : isMyWishesChecked }">
                    Мои желания
                </li>
            </router-link>

            <router-link to="/fulfilled_wishes">
                <li v-bind:class="{ 'selected-menu-item' : isFulfilledWishesChecked }">
                    Исполненные желания
                </li>
            </router-link>

            <router-link to="/planned_gifts">
                <li v-bind:class="{ 'selected-menu-item' : isPlannedGiftsChecked }">
                    Хочу подарить
                </li>
            </router-link>
        </menu>
    </menu>
</template>

<script>
export default {
    data() {
        return {
            isMyWishesChecked: false,
            isFriendsChecked: false,
            isFulfilledWishesChecked: false,
            isPlannedGiftsChecked: false
        }
    },
    watch: {
        $route() {
            this.removeSelection();
            switch(document.title) {
                case 'Мои желания':
                    this.isMyWishesChecked = true;
                    break;
                case 'Друзья':
                    this.isFriendsChecked = true;
                    break;
                case 'Заявки в друзья':
                    this.isFriendsChecked = true;
                    break;
                case 'Исполненные желания':
                    this.isFulfilledWishesChecked = true;
                    break;
                case 'Хочу подарить':
                    this.isPlannedGiftsChecked = true;
                    break;
            }
        }
    },
    methods: {
        removeSelection() {
            this.isMyWishesChecked = false;
            this.isFriendsChecked = false;
            this.isFulfilledWishesChecked = false;
            this.isPlannedGiftsChecked = false;
        }
    }
}
</script>

<style scoped>
menu {
    font-family: "Poiret One";
    min-width: 165px;
    padding: 0;
    margin-top: 70px;
}

menu a {
    font-size: 20px;
    line-height: 23px;
    color: #000000;
    text-decoration: none;
}

menu a li {
    padding: 12px 17px;
    list-style-type: none;
}

.selected-menu-item {
    background: #C6A960;
}
</style>
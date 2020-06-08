<template>
    <menu class="app-menu">
        <menu>
            <li class="selected-menu-item"><router-link to="/fiends">Друзья</router-link></li>
            <li><router-link to="/mywishes">Мои желания</router-link></li>
            <li><router-link to="/fulfilled_wishes">Исполненные желания</router-link></li>
            <li><router-link to="/planned_gifts">Хочу подарить</router-link></li>
        </menu>
    </menu>
</template>

<style scoped>
menu {
font-family: "Poiret One";
min-width: 165px;
padding: 0;
margin-top: 78px;
}

menu li {
    padding: 12px;
    list-style-type: none;
}

menu li a {
    font-size: 20px;
    line-height: 23px;
    text-align: center;
    color: #000000;
    text-decoration: none;
}

menu .selected-menu-item {
    background: #C6A960;
}
</style>
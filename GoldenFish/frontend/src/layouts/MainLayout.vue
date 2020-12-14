<template>
    <div class="content">
        <header-layout/>
        <div class="page-content cristmas">
            <menu-layout/>
            <div class="app-main-layout">
                <router-view/>
            </div>
        </div>
    </div>
</template>

<script>
import HeaderLayout from './HeaderLayout'
import MenuLayout from './MenuLayout.vue'

export default {
    components: {
        HeaderLayout,
        MenuLayout
    }
}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Poiret+One);
.content {
    font-family: "Poiret One";
    min-height: 100%;
}
.page-content {
    display: flex;
    background: rgba(168, 143, 143, 0.3);
    min-height: 92vh;
    width: 100%;
    min-width: 900px;
}

.cristmas {
    background: rgba(168, 143, 143, 0.3) url('../assets/img/snowflake.png') no-repeat 130% 50%;
    background-size: 92vh;
}

.app-main-layout {
    background: rgba(255, 255, 255, 0.5);
    width: 100%;
}
button:active, button:focus, input:active, input:focus, textarea:active, textarea:focus {
  outline: none;
}
button::-moz-focus-inner, input::-moz-focus-inner, textarea::-moz-focus-inner {
  border: 0;
}

@media (min-width: 1000px) { 
    .app-main-layout {
        margin-right: 125px;
    }
}

</style>

<style>
.spinner {
    margin: 40vh auto;
}
</style>
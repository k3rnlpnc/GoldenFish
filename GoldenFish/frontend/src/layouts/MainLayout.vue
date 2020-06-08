<template>
    <div class="content">
        <header-layout/>
        <div class="page-content">
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
.page-content {
    display: flex;
    background: rgba(168, 143, 143, 0.3);
    min-height: 92vh;
}
.app-main-layout {
    background: rgba(255, 255, 255, 0.5);
    width: 100%;
    margin-right: 125px;
}
</style>
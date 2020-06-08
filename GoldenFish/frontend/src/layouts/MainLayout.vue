<template>
    <div class="contain">
        <header-layout/>
        <div class="page-contant">
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
</script>>
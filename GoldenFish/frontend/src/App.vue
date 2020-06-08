<template>
    <div id="app">
        <component :is="layout">
            <router-view/>
        </component>
    </div>
</template>

<script>
import EmptyLayout from './layouts/EmptyLayout';
import MainLayout from './layouts/MainLayout'

export default {
    computed: {
        currentUser() {
            return this.$store.state.auth.user;
        },
        layout() {
            if(this.currentUser)
                return 'main-layout';
            else
                return 'main-layout';
        }
    },
    components : {
        EmptyLayout, MainLayout
    }
};
</script>
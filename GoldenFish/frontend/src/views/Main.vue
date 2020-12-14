<template>
    <div>
    </div>
</template>

<script>

export default {
    name: 'Main',
    mounted() {
        document.title = "Вход";
        
        if (this.$store.state.auth.status.loggedIn) {
            this.$router.push('/mywishes');
        }
        else {
            this.$router.push('/home');
        }
    }
}
</script>
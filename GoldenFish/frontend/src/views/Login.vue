<template>
    <div class="container">
        <div class="site-title">
            <span class="site-name">Golden Fish</span>
        </div>
        <form form name="form" @submit.prevent="handleLogin">
            <div>
                <span v-if="message" class="error">{{message}}</span>
            </div>

            <input 
                v-model="user.email"
                type="email" 
                name="email" 
                placeholder="Email *"
                autocomplete="off"
            />

            <input
                v-model="user.password"
                type="password"
                name="password"
                placeholder="Пароль *"
            />

            <input 
              type="submit" 
              name="login" 
              value="Войти" 
              class="button"
            />

        </form>
    </div>
</template>

<script>
import User from '../models/user';

export default {
    name: 'Login',
    data() {
        return {
        user: new User('', '', '', '', '', null),
        loading: false,
        message: ''
        };
    },
    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        }
    },
    mounted() {
        document.title = "Аутентификация";
        if (this.loggedIn) {
            this.$router.push('/mywishes');
        }
    },
    methods: {
        handleLogin() {
            this.loading = true;
            this.message = '';
            if(!this.user.email || !this.user.password)
                this.message = 'Введите email и пароль';
            else if(!this.isEmailValid())
                this.message = 'Некорректный email';
            else {
                this.$store.dispatch('auth/login', this.user).then(
                () => {
                        this.$router.push('/mywishes');
                    },
                    error => {
                        this.loading = false;
                        this.message =
                        (error.response && error.response.data) ||
                        error.message ||
                        error.toString();
                        this.message = 'Неверный email и/или пароль';
                    }        
                );
            }
        },
        isEmailValid() {
            const email = this.user.email;
            const regexp = RegExp('.@.');
            if(!regexp.test(email)) {
                this.message = 'Некорректный email';
                return false;
            }
            else
                return true;
        }
    }
};
</script>

<style scoped>
.site-title {
    display: flex;
    justify-content: center;
}

.site-name {
    height: 54px;
    font-family: "Ovo";
    font-size: 48px;
    line-height: 54px;
    color: #D8B661;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

form * {
    margin-top: 34px;
}

input{
    background-color: #6C3F5E;
    width: 315px;
    border: 0;
    border-bottom: 1px solid #A88F8F;
    color: #A88F8F;
}

input::-webkit-input-placeholder { 
    color: #A88F8F;
}

.button {
    width: 194px;
    height: 31px;
    background: #C6A960;
    font-family: Poiret One;
    font-size: 20px;
    line-height: 23px;
    text-align: center;
    color: #000000;
    border: 0;
    margin-top: 55px;
}

.button:hover {
    font-weight: bold;
}

.error {
    font-family: Poiret One;
    font-size: 20px;
    line-height: 23px;
    font-style: normal;
    font-weight: bold;
    color: #000000;
}
</style>
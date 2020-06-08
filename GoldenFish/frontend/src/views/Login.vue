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
                v-validate="'required|min:2|max:100'"
                type="email" 
                name="email" 
                placeholder="Email *"
            />

            <input
                v-model="user.password"
                v-validate="'required|min:5|max:50'"
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
      user: new User('', ''),
      loading: false,
      message: ''
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/profile');
    }
  },
  methods: {
    handleLogin() {
      this.loading = true;
      this.$validator.validateAll().then(isValid => {
        if (!isValid) {
          this.loading = false;
          return;
        }

        if (this.user.username && this.user.password) {
          this.$store.dispatch('auth/login', this.user).then(
            () => {
              this.$router.push('/profile');
            },
            error => {
              this.loading = false;
              this.message =
                (error.response && error.response.data) ||
                error.message ||
                error.toString();
            }
          );
        }
      });
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
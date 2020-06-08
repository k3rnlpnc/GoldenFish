<template>
  <div class="container">
    <form name="form" @submit.prevent="handleRegister">

        <div class="site-title">
            <span class="site-name">Golden Fish</span>
        </div>

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
        v-model="user.username"
        v-validate="'required|min:3|max:50'"
        type="text"
        name="username"
        placeholder="Юзернейм *"
      />

      <input
        v-model="user.name"
        v-validate="'required|min:2|max:50'"
        type="text"
        name="name"
        placeholder="Имя *"
      />

      <input
        v-model="user.surname"
        v-validate="'required|min:2|max:50'"
        type="text"
        name="surname"
        placeholder="Фамилия *"
      />

      <input
        v-model="user.password"
        v-validate="'required|min:5|max:50'"
        type="password"
        name="password"
        placeholder="Пароль *"
      />

      <input
        v-model="user.birthday"
        type="date"
        name="birtday"
      />

      <input
        type="submit"
        value="Зарегистрироваться"
        class="button"
      />

    </form>
  </div>
</template>

<script>
import User from '../models/user';

export default {
  name: 'Register',
  data() {
    return {
      user: new User('', '', '', '', '', null),
      submitted: false,
      successful: false,
      message: ''
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push('/profile');
    }
  },
  methods: {
    handleRegister() {
      this.message = '';
      this.submitted = true;
      this.$validator.validate().then(isValid => {
        if (isValid) {
          this.$store.dispatch('auth/register', this.user).then(
            data => {
              this.message = data.message;
              this.successful = true;
            },
            error => {
              this.message =
                (error.response && error.response.data) ||
                error.message ||
                error.toString();
              this.successful = false;
            }
          );
        }
      });
    }
  }
};
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Ovo);
@import url(https://fonts.googleapis.com/css?family=Poiret+One);

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
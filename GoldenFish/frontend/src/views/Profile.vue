<template>
    <div class="container">
        <h3 class="ptofile-title">Профиль</h3>
            <form method="form" class="edit-profile-form">
                <input 
                    name="username"
                    placeholder="Username"
                    required
                />

                <input 
                    type="email" 
                    name="email" 
                    placeholder="user@mail.ru" 
                    required>

                <input 
                    name="name" 
                    placeholder="Иван" 
                    autocomplete="off" 
                    required
                />

                <input 
                    name="surname" 
                    placeholder="Иванов" 
                    autocomplete="off" 
                    required
                    />

                <input 
                    type="date" 
                    name="birthday" 
                />

                <input 
                    type="submit" 
                    name="edit_profile" 
                    value="Сохранить"
                />
            </form>
    </div>
</template>

<script>
export default {
  name: 'Profile',
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    }
  }
  /*mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
  }*/
};
</script>

<style scoped>
.ptofile-title {
    text-align: center;
    margin: 80px 80px 40px 80px;
    font-size: 30px;
    line-height: 35px;
    color: #6C3F5E;;
}

.edit-profile-form {
    margin: 0px 30px;
    display: flex;
    flex-direction: column; 
}

.edit-profile-form input {
    background: inherit;
    border: 0;
    border-bottom: 1px solid rgba(140, 102, 128, 0.5);
    margin-bottom: 35px;
    padding: 7px 25px;
    font-size: 15px;
    line-height: 18px;
    color: #6C3F5E;; 
}

.edit-profile-form input::-webkit-input-placeholder { 
    font-size: 15px;
    line-height: 18px;
    color: #6C3F5E; 
}

.edit-profile-form input[type="submit"] {
    border: 0;
    cursor: pointer;
}
</style>
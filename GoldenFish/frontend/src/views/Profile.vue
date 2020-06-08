<template>
    <div class="container">
        <h3 class="ptofile-title">Профиль</h3>
            <div class="error">{{message}}</div>

            <form name="form" class="edit-profile-form" @submit.prevent="editProfile">
                <input 
                    v-model="user.username"
                    name="username"
                />

                <input 
                    v-model="user.email"
                    type="email" 
                    name="email" 
                />

                <input 
                    v-model="user.name"
                    name="name" 
                    autocomplete="off" 
                />

                <input 
                    v-model="user.surname"
                    name="surname" 
                    autocomplete="off" 
                />

                <input 
                    v-model="user.birthday"
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
import ProfileService from '../services/profile.service';
import User from '../models/user';

export default {
    name: 'Profile',
    data() {
        return {
            message: '',
            user : new User()
        }
    },
    computed: {
        currentUser() {
            return this.$store.state.auth.user;
        }
    },
    mounted() {
        document.title = "Профиль";
        if(!this.currentUser)
            this.$router.push('/');
        ProfileService.getProfileInfo().then(
            response => {
                this.user = response.data;
            }
        );
    },
    methods: {
        editProfile() {
            this.message = '';
            let editUser = new User('', '', '', '', '');
            if(!this.user.birthday)
            {
                editUser.email = this.user.email;
                editUser.username = this.user.username;
                editUser.name = this.user.name;
                editUser.surname = this.user.surname;
            }
            else {
                editUser = this.user;
            }
            if (this.isFormValid()) {
                ProfileService.editProfile(editUser).then(
                    () => {
                        this.message = 'Профиль успешно отредактирован';
                    },
                    error => {
                        this.message =
                        (error.response + error.response.data) ||
                        error.message ||
                        error.toString();
                        this.message = 'Email и/или юзернейм уже существует';
                        this.successful = false;
                    }
                );
            }
        },
        isFormValid() {
            if(this.user.email === '' ||  this.user.username === '' || 
            this.user.name === '' || this.user.surname === '') {
                this.message = 'Не все обязательные поля заполенены';
                return false;
            }  
            else if(!this.isEmailValid() || !this.isUsernameValid() || 
            !this.isNameValid() || !this.isSurnameValid()) {
                return false;
            }
            else
                return true;             
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
        },
        isUsernameValid() {
            const username = this.user.username;
            const regexp = RegExp('^[^a-zA-Zа-яА-Я]');
            if(username.length < 3 || regexp.test(username)) {
                this.message = 'Юзернейм должен содержать минимум 3 символа и не начинаться с цифры или специального символа';
                return false;
            }
            else
                return true;
        },
        isNameValid() {
            const name = this.user.name;
            const regexp = RegExp('[^a-zA-Zа-яА-Я]');
            if(name.length < 2 || regexp.test(name)) {
                this.message = 'Имя должно содержать минимум 2 символа и состоять из символов латинского или русского алфавита';
                return false;
            }
            else
                return true;
        },
        isSurnameValid() {
            const surname = this.user.surname;
            const regexp = RegExp('[^a-zA-Zа-яА-Я]');
            if(surname.length < 2 || regexp.test(surname)) {
                this.message = 'Фамилия должна содержать минимум 2 символа и состоять из символов латинского или русского алфавита';
                return false;
            }
            else
                return true;
        }
    }
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
.error {
    font-family: Poiret One;
    text-align: center;
    font-size: 20px;
    line-height: 23px;
    font-style: normal;
    font-weight: bold;
    color: #000000;
    margin-bottom: 10px;
}
</style>
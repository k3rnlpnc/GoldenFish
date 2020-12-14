import axios from 'axios';

const API_URL = 'https://golden-fish-api.herokuapp.com/';

class AuthService {
    login(user) {
        return axios.post(API_URL + 'authentication', {
            email: user.email,
            password: user.password
        })
        .then(
            response => {
                if (response.data.access_token) {
                    localStorage.setItem('user', JSON.stringify(response.data.access_token));
                }
                return Promise.resolve(response.data);
            }, 
            error => {
                return Promise.reject(error);
            }
        );
    }

    logout() {
        localStorage.removeItem('user');
    }

    register(user) {
        return axios.post(API_URL + 'registration', {
        email: user.email,
        password: user.password,
        username: user.username,
        name: user.name,
        surname: user.surname,
        birthday: user.birthday
        }).then(
            response => {
                if (response.data.access_token) {
                    localStorage.setItem('user', JSON.stringify(response.data.access_token));
                }
                return Promise.resolve(response.data);
            }, 
            error => {
                return Promise.reject(error);
            }
        );
    }
}

export default new AuthService();

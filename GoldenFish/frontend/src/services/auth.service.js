import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/';

class AuthService {
  login(user) {
    return axios
      .post(API_URL + 'authentication', {
        email: user.email,
        password: user.password
      })
      .then(
        response => {
          if (response.data.access_token) {
            localStorage.setItem('user', JSON.stringify(response.data.access_token));
          }
          // TODO: should it be: return response.data.access_token ?
          return Promise.resolve(response.data);
        }, 
        error => {
          return Promise.reject(error);
      });
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
    });
  }
}

export default new AuthService();

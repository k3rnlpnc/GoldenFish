import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/';

class AuthService {
  login(user) {
    return axios
      .post(API_URL + 'signin', {
        username: user.username,
        password: user.password
      })
      .then(response => {
        if (response.data.accessToken) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
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

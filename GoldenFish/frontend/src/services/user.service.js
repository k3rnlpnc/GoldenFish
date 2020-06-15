import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://127.0.0.1:5000/';

class UserService {
    getUserInfo(id) {
        return axios.get(API_URL + 'users/' + id, { headers: authHeader() });
    }

    getProfileInfo() {
        return axios.get(API_URL + 'profile', { headers: authHeader() });
    }

    findFriendByUsername(username) {
        return axios({
            method: 'post',
            url: API_URL + 'users',
            headers: authHeader(),
            data: {
                username: username
            }
        });
    }
}

export default new UserService();

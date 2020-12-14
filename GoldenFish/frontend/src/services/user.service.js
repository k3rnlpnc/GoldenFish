import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'https://golden-fish-api.herokuapp.com/';

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

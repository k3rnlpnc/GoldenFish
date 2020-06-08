import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://127.0.0.1:5000/';

class ProfileService {
    getProfileInfo() {
        return axios.get(API_URL + 'profile', { headers: authHeader() });
    }

    editProfile(user) {
        return axios({
            method: 'put',
            url: API_URL + 'profile',
            headers: authHeader(),
            data: {
                email: user.email,
                username: user.username,
                name: user.name,
                surname: user.surname,
                birthday: user.birthday
            }
        });
    }
}

export default new ProfileService();
import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'https://golden-fish-api.herokuapp.com/';

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
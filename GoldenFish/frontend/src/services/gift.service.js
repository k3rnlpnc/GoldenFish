import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'https://golden-fish-api.herokuapp.com/';

class GiftService {
    getGifts() {
        return axios.get(API_URL + 'gifts', { headers: authHeader() });
    }

    addGift(friend_id, dream_id) { 
        return axios({
            method: 'put',
            url: API_URL + 'friends/'+ friend_id + '/' + dream_id,
            headers: authHeader(),
            data: {
                friend_id: friend_id,
                dream_id: dream_id
            }
        });
    }

    deleteGift(id) {
        return axios.delete(API_URL + 'gifts/' + id, { headers: authHeader() });
    }
}

export default new GiftService();
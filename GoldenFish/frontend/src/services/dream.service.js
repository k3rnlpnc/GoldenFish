import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'https://golden-fish-api.herokuapp.com/';

class DreamService {
    getMyWishes() {
        return axios.get(API_URL + 'mywishes', { headers: authHeader() });
    }

    getWishInfo(id) {
        return axios({
            method: 'get',
            url: API_URL + 'mywishes/' + id,
            headers: authHeader(),
            data: {
                dream_id: id
            }
        });
    }

    getFriendWish(dream_id) {
        return axios({
            method: 'get',
            url: API_URL + 'friends/dreams/' + dream_id,
            headers: authHeader(),
            data: {
                dream_id: dream_id
            }
        });
    }

    addWish(wish) {
        return axios({
            method: 'post',
            url: API_URL + 'mywishes',
            headers: authHeader(),
            data: {
                name: wish.name,
                description: wish.description,
                store_link: wish.store_link,
                image_link: wish.image_link,
                is_fulfilled: false
            }
        });
    }

    deleteWish(id) {
        return axios.delete(API_URL + 'mywishes/' + id, { headers: authHeader() });
    }

    editWish(wish) {
        return axios({
            method: 'put',
            url: API_URL + 'mywishes/' + wish.id,
            headers: authHeader(),
            data: {
                name: wish.name,
                description: wish.description,
                store_link: wish.store_link,
                image_link: wish.image_link,
            }
        });
    }

    setWishFulfilled(id) {
        return axios({
            method: 'put',
            url: API_URL + 'mywishes/' + id,
            headers: authHeader(),
            data: {
                is_fulfilled: true
            }
        });
    }

    getFulfilledWishes() {
        return axios.get(API_URL + 'fulfilled', { headers: authHeader() });
    }
}

export default new DreamService();
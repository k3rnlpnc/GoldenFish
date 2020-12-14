import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'https://golden-fish-api.herokuapp.com/';

class FriendService {
    getFriends() {
        return axios.get(API_URL + 'friends', { headers: authHeader() });
    }

    getFriendRequests() {
        return axios.get(API_URL + 'friends/requests', { headers: authHeader() });
    }

    addFriend(user_id) {
        return axios({
            method: 'put',
            url: API_URL + 'users/' + user_id,
            headers: authHeader(),
            data: {
                user_id: user_id
            }
        });
    }

    deleteFriend(user_id) {
        return axios.delete(API_URL + 'friends/' + user_id, { headers: authHeader() });
    }

    acceptRequest(sender_id) {
        return axios({
            method: 'put',
            url: API_URL + 'friends/requests/' + sender_id,
            headers: authHeader(),
            data: {
                sender_id: sender_id
            }
        });
    }

    rejectRequest(sender_id) {
        return axios.delete(API_URL + 'friends/requests/' + sender_id, { headers: authHeader() });
    }

    getFriendWishes(friend_id) {
        return axios({
            method: 'get',
            url: API_URL + 'friends/' + friend_id,
            headers: authHeader(),
            data: {
                friend_id: friend_id
            }
        });
    }
}

export default new FriendService();
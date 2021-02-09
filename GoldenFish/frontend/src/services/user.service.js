import { instance } from "./api";

class UserService {
    getUserInfo(id) {
        return instance.get('users/' + id);
    }

    getProfileInfo() {
        return instance.get('profile');
    }

    findFriendByUsername(username) {
        return instance.post('users', { username: username });
    }
}

export default new UserService();
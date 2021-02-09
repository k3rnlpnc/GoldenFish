import { instance } from "./api";

class ProfileService {
    getProfileInfo() {
        return instance.get('profile');
    }

    editProfile(user) {
        return instance.put('profile', {
            email: user.email,
            username: user.username,
            name: user.name,
            surname: user.surname,
            birthday: user.birthday
        });
    }
}

export default new ProfileService();
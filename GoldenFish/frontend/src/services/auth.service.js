import { instance } from "./api";

class AuthService {
    login(user) {
        return instance.post('authentication', {
            email: user.email,
            password: user.password
        })
            .then(
                response => {
                    if (response.data.access_token) {
                        localStorage.setItem('user', JSON.stringify(response.data.access_token));
                    }
                    return Promise.resolve(response.data);
                },
                error => {
                    return Promise.reject(error);
                }
            );
    }

    logout() {
        localStorage.removeItem('user');
    }

    register(user) {
        return instance.post('registration', {
            email: user.email,
            password: user.password,
            username: user.username,
            name: user.name,
            surname: user.surname,
            birthday: user.birthday
        }).then(
            response => {
                if (response.data.access_token) {
                    localStorage.setItem('user', JSON.stringify(response.data.access_token));
                }
                return Promise.resolve(response.data);
            },
            error => {
                return Promise.reject(error);
            }
        );
    }
}

export default new AuthService();

export default class User {
    constructor(email, password, username='', name='', surname='', birthday) {
        this.email = email;
        this.password = password;
        this.username = username;
        this.name = name;
        this.surname = surname;
        this.birthday = birthday
    }
}
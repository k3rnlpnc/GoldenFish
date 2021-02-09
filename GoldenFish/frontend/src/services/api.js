import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'https://golden-fish-api.herokuapp.com/';

export const instance = axios.create({
    baseURL: API_URL,
    headers: authHeader()
});
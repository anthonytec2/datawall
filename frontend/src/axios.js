import axios from 'axios';
const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000/'
  });
  instance.defaults.headers.common['Authorization'] = 'AUTH TOKEN FROM INSTANCE';
  export default instance;
  
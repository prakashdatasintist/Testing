// // // // api.js
// // // import axios from 'axios';

// // // const API = axios.create({
// // //   baseURL: 'http://localhost:8000/api/',
// // // });

// // // export const login = (data) => API.post('/login/', data);
// // // export const register = (data) => API.post('/register/', data);
// // // // export const fetchUsers = () => API.get('/users/');
// // // export const fetchUsers = () => API.get('/users/'); // Adjusted endpoint
// // // export const sendInterest = (data) => API.post('/main/interests/', data);
// // // export const fetchInterests = () => API.get('/main/interests/');
// // // export const sendMessage = (data) => API.post('/main/chats/', data);
// // // export const fetchMessages = (chatId) => API.get(`/main/chats/${chatId}/`);
// // // src/api.js
// import axios from 'axios';

// const API = axios.create({
//   baseURL: 'http://localhost:8000/api/',
// });

// export const login = (data) => API.post('/login/', data);
// export const register = (data) => API.post('/register/', data);
// export const fetchUsers = () => API.get('/users/');
// export const sendInterest = (data) => API.post('/main/interests/', data);
// export const fetchInterests = () => API.get('/main/interests/');
// export const sendMessage = (data) => API.post('/main/chats/', data);
// export const fetchMessages = (chatId) => API.get(`/main/chats/${chatId}/`);
// // import axios from 'axios';

// // const API = axios.create({
// //   baseURL: 'http://localhost:8000/api/',
// // });

// export default API;
// src/api.js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export const login = (data) => API.post('/login/', data);
export const register = (data) => API.post('/register/', data);
export const fetchUsers = () => API.get('/users/');
export const sendInterest = (data) => API.post('/main/interests/', data);
export const fetchInterests = () => API.get('/main/interests/');
export const sendMessage = (data) => API.post('/main/chats/', data);
export const fetchMessages = (chatId) => API.get(`/main/chats/${chatId}/`);

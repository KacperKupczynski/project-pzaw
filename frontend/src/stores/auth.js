import { writable } from 'svelte/store';

const storedToken = localStorage.getItem('authToken');
const storedUsername = localStorage.getItem('username');

export const auth = writable({
    isAuthenticated: !!storedToken,
    token: storedToken,
    username: storedUsername,
});

export function login(token, username) {
    auth.set({
        isAuthenticated: true,
        token: token,
        username: username,
    });
    localStorage.setItem('authToken', token);
    localStorage.setItem('username', username);
}

export function logout() {
    auth.set({
        isAuthenticated: false,
        token: null,
        username: null,
    });
    localStorage.removeItem('authToken');
    localStorage.removeItem('username');
}
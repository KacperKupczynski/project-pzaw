import { writable } from 'svelte/store';

export const auth = writable({
    isAuthenticated: false,
    token: null,
    username: null,
});

export function login(token, username) {
    auth.set({
        isAuthenticated: true,
        token,
        username,
    });
}

export function logout() {
    auth.set({
        isAuthenticated: false,
        token: null,
        username: null,
    });
    localStorage.removeItem('authToken');
}
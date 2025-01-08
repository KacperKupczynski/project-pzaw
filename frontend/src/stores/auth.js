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
    localStorage.removeItem('refreshToken');
}

export async function refreshToken() {
    const refreshToken = localStorage.getItem('refreshToken');
    if (refreshToken) {
        const response = await fetch('/api/token/refresh/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ refresh: refreshToken }),
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('authToken', data.access);
            auth.update(state => ({ ...state, token: data.access }));
        } else {
            logout();
        }
    } else {
        logout();
    }
}
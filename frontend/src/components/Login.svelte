<script>
import { login } from '../stores/auth.js';
import { onMount } from 'svelte';

let username = '';
let password = '';
let errorMessage = '';

    async function handleLogin() {
        try {
            const response = await fetch('/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                throw new Error('Invalid credentials');
            }

            const data = await response.json();
            login(data.access, username); // Ustaw token i użytkownika
            localStorage.setItem('authToken', data.access);
            errorMessage = '';
        } catch (error) {
            errorMessage = error.message;
        }
    }
</script>

<div>
    <h2>Login</h2>
    <form on:submit|preventDefault={handleLogin}>
        <input type="text" bind:value={username} placeholder="Username" required />
        <input type="password" bind:value={password} placeholder="Password" required />
        <button type="submit">Log in</button>
    </form>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
</div>
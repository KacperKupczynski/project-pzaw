<script>
    import { navigate } from 'svelte-routing';
    import { login } from '../stores/auth.js';

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
            login(data.token, data.username); // Use the login function from auth.js
            localStorage.setItem('authToken', data.access); // Store the access token in localStorage
            localStorage.setItem('refreshToken', data.refresh); // Store the refresh token in localStorage
            errorMessage = '';
            navigate('/'); // Redirect to home page
        } catch (error) {
            errorMessage = error.message;
        }
    }
</script>

<main>
    <h2>Login</h2>
    <form on:submit|preventDefault={handleLogin}>
        <input type="text" bind:value={username} placeholder="Username" required />
        <input type="password" bind:value={password} placeholder="Password" required />
        <button type="submit">Log in</button>
    </form>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    <p>or make an account here:
        <a href="/register">Register</a>
    </p>
</main>

<style>
    input {
        margin-top: 10px;
    }
</style>
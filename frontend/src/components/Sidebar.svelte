<script>
    import { auth, logout, refreshToken } from '../stores/auth.js';
    import { onMount } from 'svelte';

    let username;

    $: username = $auth.username;

    async function handleLogout() {
        try {
            const response = await fetch('/api/logout/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                },
                credentials: 'include'
            });

            if (!response.ok) {
                throw new Error('Failed to logout');
            }

            logout();
            window.location.href = '/login'; // Redirect to login page after logout
        } catch (error) {
            console.error('Logout failed:', error);
        }
    }

    onMount(() => {
        const token = localStorage.getItem('authToken');
        const username = localStorage.getItem('username');
        if (token && username) {
            auth.update(state => ({ ...state, isAuthenticated: true, token, username }));
        }
        refreshToken();
    });
    </script>

<nav>
    <a href="/">
        <img src="/logo.png" alt="Logo" />
    </a>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/typeracer">Type Racing</a></li>
        <li><a href="/addtext">Add text</a></li>
        <li><a href="/list">List of texts</a></li>
    </ul>
    <div class="user-info">
        {#if username}
            <p>{username}</p>
            <button on:click={handleLogout}>Logout</button>
        {:else}
            <p>Not logged in</p>
            <a href="/login">Login</a>
        {/if}
    </div>
</nav>

<style>
    nav {
        height: 8rem;
        display: flex;
        align-items: center;
        justify-content: space-evenly;
    }
    
    ul {
        display: flex;
        list-style-type: none;
        gap: 1rem;
    }
    li {
        margin-right: 10px;
    }
    li:hover {
        font-weight: bold;
    }
    button {
        cursor: pointer;
    }
</style>
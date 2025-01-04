<script>
    import { auth, logout } from '../stores/auth.js';
    import { onMount } from 'svelte';

    let username;

    $: username = $auth.username;

    function handleLogout() {
        logout();
        window.location.href = '/login'; // Redirect to login page after logout
    }

    onMount(() => {
        const token = localStorage.getItem('authToken');
        if (token) {
            auth.update(state => ({ ...state, isAuthenticated: true, token }));
        }
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
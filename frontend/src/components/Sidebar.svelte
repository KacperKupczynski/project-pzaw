<script>
    import { navigate } from 'svelte-routing';
    import { auth, logout } from '../stores/auth.js';

    let username;

    $: username = $auth.username;

    function handleLogout() {
        logout();
        window.location.href = '/login'; // Redirect to login page after logout
    }
</script>

<nav>
    <a href="/">
        <img src="/logo.png" alt="Logo" />
    </a>
    <ul>
        <!-- to do - use navigate from svelte routing instead -->
        <li><a href="/">Home</a></li>
        <li><a href="/typeracer">Type Racing</a></li>
        <li><a href="/addtext">Add text</a></li>
        <li><a href="/list">List of texts</a></li>
        <li><a href="/results">Your Results</a></li>
    </ul>
    <div class="user-info">
        {#if $auth.isAuthenticated}
            <p>{$auth.username}</p>
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
        background: linear-gradient(179.985deg, #000000 0%, rgba(22, 22, 22, 79%) 58%, rgba(41, 41, 41, 0) 100%);
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
<script>
    import { auth, logout } from '../stores/auth.js';
    import { get } from 'svelte/store';

    let username;
    $: username = $auth.username;

    function handleLogout() {
        logout();
        window.location.href = '/login'; // Redirect to login page after logout
    }
</script>

<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/typeracer">Type Racing</a></li>
        <li><a href="/addtext">Add text</a></li>
        <li><a href="/list">Text list</a></li>
    </ul>
    <div>
        <p>Logged in as: {username}</p>
        <button on:click={handleLogout}>Logout</button>
    </div>
</nav>

<style>
    nav {
        width: 200px;
        background-color: #383838;
        height: 100vh;
        padding: 20px;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin: 10px 0;
        cursor: pointer;
    }
    li:hover {
        font-weight: bold;
    }
    div {
        margin-top: 20px;
    }
    button {
        margin-top: 10px;
        padding: 5px 10px;
        cursor: pointer;
    }
</style>
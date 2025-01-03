<script>
  import LoginForm from './components/Login.svelte';
  import RegisterForm from './components/Register.svelte';
  import { auth, logout } from './stores/auth.js';

  let user = null;

  $: auth.subscribe((state) => {
      user = state;
  });

  function handleLogout() {
      logout();
  }
</script>

<main>
  {#if user.isAuthenticated}
      <h1>Welcome, {user.username}!</h1>
      <button on:click={handleLogout}>Logout</button>
  {:else}
      <LoginForm />
      <RegisterForm />
  {/if}
</main>

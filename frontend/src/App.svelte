<script>
  import { Router, Route, Link } from 'svelte-routing';
  import Home from './components/Home.svelte';
  import Sidebar from './components/Sidebar.svelte';
  import TypeRacer from './components/TypeRacer.svelte';
  import Login from './components/Login.svelte';
  import Addtext from './components/Addtext.svelte';
  import TextList from './components/TextList.svelte';
  import Register from './components/Register.svelte';
  import { auth } from './stores/auth.js';
  import UserResults from './components/UserResults.svelte';
  import { onMount } from 'svelte';

  let isAuthenticated;
  $: isAuthenticated = $auth.isAuthenticated;

  onMount(() => {
    const token = localStorage.getItem('authToken');
    if (token) {
      auth.update(state => ({ ...state, isAuthenticated: true, token }));
    }
  });
</script>

{#if isAuthenticated}
  <Router>
    <Sidebar />
    <Route path="/" component={Home} />
    <Route path="/typeracer" component={TypeRacer} />
    <Route path="/addtext" component={Addtext} />
    <Route path="/list" component={TextList} />
    <Route path="/login" component={Login} />
    <Route path="/results" component={UserResults} />
  </Router>
{:else}
  <Router>
    <Route path="/" component={Login} />
    <Route path="/login" component={Login} />
    <Route path="/register" component={Register} />
  </Router>
{/if}

<style>
  :global(body) {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    margin: 0;
    padding: 0;
  }
</style>
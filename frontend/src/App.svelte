<script>
  let users = [];

  const fetchUsers = async () => {
      const response = await fetch('/api/users/');
      users = await response.json();
  };

  fetchUsers();
</script>

<h1>Lista użytkowników</h1>
<ul>
  {#each users as user}
      <li>{user.name} ({user.email})</li>
  {/each}
</ul>
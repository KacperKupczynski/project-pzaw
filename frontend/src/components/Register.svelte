<script>
    import { navigate } from "svelte-routing";

    let username = '';
    let password = '';
    let successMessage = '';
    let errorMessage = '';

    async function handleRegister() {
        try {
            const response = await fetch('/api/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                throw new Error('Registration failed');
            }

            successMessage = 'Registration successful! You can now log in.';
            errorMessage = '';
            username = '';
            password = '';
        } catch (error) {
            errorMessage = error.message;
        }
    }
</script>

<div>
    <h2>Register</h2>
    <form on:submit|preventDefault={handleRegister}>
        <input type="text" bind:value={username} placeholder="Username" required />
        <input type="password" bind:value={password} placeholder="Password" required />
        <button type="submit">Register</button>
    </form>
    {#if successMessage}
        <p style="color: green;">{successMessage}</p>
        <button on:click={navigate("/login")}>Login</button>
    {/if}
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
</div>

<script>
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';

    let content = '';
    let errorMessage = '';
    let successMessage = '';

    async function handleAddText() {
        try {
            const response = await fetch('/api/texts/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                },
                body: JSON.stringify({ content }),
            });

            if (!response.ok) {
                throw new Error('Failed to add text');
            }

            successMessage = 'Text added successfully!';
            errorMessage = '';
            content = '';
        } catch (error) {
            errorMessage = error.message;
            successMessage = '';
        }
    }
</script>

<div>
    <h2>Add Text</h2>
    <form on:submit|preventDefault={handleAddText}>
        <textarea bind:value={content} placeholder="Enter text here" required></textarea>
        <button type="submit">Add Text</button>
    </form>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    {#if successMessage}
        <p style="color: green;">{successMessage}</p>
    {/if}
</div>

<style>
    textarea {
        width: 100%;
        height: 100px;
        margin-top: 10px;
    }
    button {
        margin-top: 10px;
        padding: 5px 10px;
        cursor: pointer;
    }
</style>
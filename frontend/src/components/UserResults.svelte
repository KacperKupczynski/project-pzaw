<script>
    import { onMount } from 'svelte';

    let results = [];
    let errorMessage = '';

    onMount(async () => {
        try {
            const response = await fetch('/api/results/', {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                },
                credentials: 'include',
            });

            if (!response.ok) {
                throw new Error('Failed to fetch results');
            }

            results = await response.json();
        } catch (error) {
            errorMessage = error.message;
        }
    });

    function formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
        return new Date(dateString).toLocaleDateString(undefined, options);
    }
</script>

<main>
    <h2>Your Results</h2>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {:else if results.length === 0}
        <p>No results yet.</p>
    {:else}
        <ul>
            {#each results as result}
                <li>
                    {result.wpm} WPM, {result.accuracy}% Accuracy, {formatDate(result.created_at)}
                </li>
            {/each}
        </ul>
    {/if}
</main>

<style>
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin-bottom: 10px;
    }
</style>
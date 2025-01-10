<script>
    import { onMount } from 'svelte';

    let results = [];
    let errorMessage = '';
    let averageWpm = 0;

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
            calculateAverageWpm();
        } catch (error) {
            errorMessage = error.message;
        }
    });

    function calculateAverageWpm() {
        if (results.length > 0) {
            const totalWpm = results.reduce((sum, result) => sum + result.wpm, 0);
            averageWpm = parseFloat((totalWpm / results.length).toFixed(2));
        }
    }

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
        <div>
            <p>Average WPM: {averageWpm}</p>
            <ul>
                {#each results as result}
                    <li>
                        {Math.round(result.wpm)} WPM, {formatDate(result.created_at)}
                    </li>
                {/each}
            </ul>
        </div>
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
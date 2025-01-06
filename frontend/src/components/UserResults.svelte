<script>
    import { onMount } from 'svelte';
    import { auth } from '../stores/auth.js';

    let results = [];
    let errorMessage = '';
    let statistics = {};

    onMount(() => {
        fetch(`/api/user/${$auth.username}/results/`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch results');
            }
            return response.json();
        })
        .then(data => {
            results = data;
        })
        .catch(error => {
            errorMessage = error.message;
        });

        fetch(`/api/user/${$auth.username}/statistics/`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch statistics');
            }
            return response.json();
        })
        .then(data => {
            statistics = data;
        })
        .catch(error => {
            errorMessage = error.message;
        });
    });
</script>

<main>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    <h2>Your Results</h2>
    <ul>
        {#each results as result}
            <li>
                <p>Text: {result.text.content}</p>
                <p>WPM: {result.wpm}</p>
                <p>Accuracy: {result.accuracy}%</p>
                <p>Date: {new Date(result.created_at).toLocaleString()}</p>
            </li>
        {/each}
    </ul>
    <h2>Your Statistics</h2>
    <p>Average WPM: {statistics.average_wpm}</p>
    <p>Average Accuracy: {statistics.average_accuracy}%</p>
    <p>Total Results: {statistics.total_results}</p>
</main>

<style>
    main {
        padding: 2rem;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin-bottom: 1rem;
        padding: 1rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    p {
        margin: 0.5rem 0;
    }
</style>
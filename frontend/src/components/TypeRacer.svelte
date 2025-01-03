<script>
    import { onMount } from 'svelte';
    import { typeRacer, updateTypeRacer } from '../stores/typeRacer.js';
    import { get } from 'svelte/store';

    let text = '';
    let input = '';
    let time = 0;
    let interval = null;
    let isRunning = false;
    let errorMessage = '';

    onMount(() => {
        fetch('/api/text/', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch text');
            }
            return response.json();
        })
        .then(data => {
            text = data.content; // Adjusted to handle a single object response
        })
        .catch(error => {
            errorMessage = error.message;
        });
    });

    function start() {
        if (isRunning) {
            return;
        }

        isRunning = true;
        time = 0;
        input = '';
        interval = setInterval(() => {
            time++;
        }, 1000);
    }

    function stop() {
        if (!isRunning) {
            return;
        }

        isRunning = false;
        clearInterval(interval);
        updateTypeRacer(time, text, input);

        const result = get(typeRacer);
        fetch('/api/results/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            },
            body: JSON.stringify({
                user: result.username, // Assuming the username is stored in the result
                text: text,
                wpm: result.wpm,
                accuracy: result.accuracy
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to submit result');
            }
            return response.json();
        })
        .catch(error => {
            errorMessage = error.message;
        });
    }
</script>

<div>
    <h2>Type Racer</h2>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    <p>{text}</p>
    <input type="text" bind:value={input} on:input={stop} />
    <button on:click={start}>Start</button>
    <button on:click={stop}>Stop</button>
</div>

<style>
    input {
        margin-top: 10px;
    }
</style>
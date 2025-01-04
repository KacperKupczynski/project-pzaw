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
    let letterStates = [];

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
            letterStates = text.split('').map(letter => ({ letter, state: 'default' }));
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
        interval = setInterval(() => {
            time += 0.01;
        }, 10);
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

    $: if (input.length === 1 && !isRunning) {
        start();
    }

    $: if (input.length === text.length) {
        stop();
    }

    function handleInput(event) {
        input = event.target.value;

        for (let i = 0; i < text.length; i++) {
            if (i < input.length) {
                if (text[i] === input[i]) {
                    letterStates[i].state = 'correct';
                } else {
                    letterStates[i].state = 'incorrect';
                }
            } else {
                letterStates[i].state = 'default';
            }
        }
    }

    function getClass(state) {
        return state === 'correct' ? 'correct' : state === 'incorrect' ? 'incorrect' : 'not-typed';
    }
</script>

<main>
    <h2>Type Racer</h2>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    <div id="displayer">
        {#each letterStates as { letter, state }, index}
            <span class={getClass(state)}>{letter}</span>
        {/each}
    </div>
    <input type="text" bind:value={input} on:input={handleInput} />

    <p>Time: {time.toFixed(2)} seconds</p>
</main>

<style>
    input {
        margin-top: 10px;
        width: 100%;
        padding: 10px;
        font-size: 16px;
    }
    .correct {
        color: green;
    }
    .incorrect {
        color: red;
    }
    .not-typed {
        color: black;
    }
</style>
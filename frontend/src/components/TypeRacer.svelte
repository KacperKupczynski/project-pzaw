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
    let wpm = 0;
    let textObject = null;
    let showModal = false;

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
            textObject = data; // Store the text object
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
            calculateWPM();
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
        console.log("Sending result:", {
            wpm: result.wpm,
            accuracy: result.accuracy
        });
        fetch('/api/result/', {  // Update the endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            },
            body: JSON.stringify({
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

        showModal = true; // Show the modal
    }

    function calculateWPM() {
        const wordsTyped = input.trim().split(/\s+/).length;
        wpm = Math.floor((wordsTyped / (time / 60)));
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

    function closeModal() {
        showModal = false;
    }

    function playAgain() {
        location.reload();
    }
</script>

<main>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    <div class="displayer">
        {#each letterStates as { letter, state }}
            <span class={getClass(state)}>{letter}</span>
        {/each}
    </div>
    <input type="text" bind:value={input} on:input={handleInput} placeholder="Enter a word here..."/>

    <p>Time: {time.toFixed(2)} seconds</p>
    <p>WPM: {wpm}</p>

    {#if showModal}
        <div class="modal">
            <div class="modal-content">
                <span class="close" on:click={closeModal}>&times;</span>
                <h2>Results</h2>
                <p>WPM: {wpm}</p>
                <button on:click={playAgain}>Play Again</button>
            </div>
        </div>
    {/if}
</main>

<style>
    main {
        padding: 4rem;
    }
    input {
        margin-top: 10px;
        padding: 10px;
        font-size: 20px;
        background: #333333;
    }
    .correct {
        color: green;
    }
    .incorrect {
        color: red;
    }
    .not-typed {
        color: rgb(151, 151, 151);
    }
    .displayer {
        color: white;
    }
    .displayer span {
        font-size: 24px;
    }
    p {
        font-size: 20px;
    }
    .modal {
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.4);
    }
    .modal-content {
        background-color: #333333;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
        max-width: 500px;
        text-align: center;
    }
    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
    }
    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
    button {
        margin-top: 20px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
</style>
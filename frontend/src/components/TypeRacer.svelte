<script>
    import { onMount } from 'svelte';
    import { typeRacer, updateTypeRacer } from '../stores/typeRacer.js';
    import { get } from 'svelte/store';
    
    let text = '';
    let input = '';
    let time = 0;
    let interval = null;
    let isRunning = false;
    
    onMount(() => {
        fetch('/api/typeracer/')
        .then(response => response.json())
        .then(data => {
            text = data.text;
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
    }
</script>

<div>
    <h2>Type Racer</h2>
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
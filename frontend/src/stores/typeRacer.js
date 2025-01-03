import { writable } from 'svelte/store';

export const typeRacer = writable({
    time: 0,
    text: '',
    input: '',
    wpm: 0,
    accuracy: 0
});

export function updateTypeRacer(time, text, input) {
    const wordsTyped = input.trim().split(/\s+/).length;
    const wpm = (wordsTyped / time) * 60;
    const accuracy = (input.length / text.length) * 100;

    typeRacer.set({
        time,
        text,
        input,
        wpm,
        accuracy
    });
}
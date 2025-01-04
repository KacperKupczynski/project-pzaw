<script>
    import { onMount } from 'svelte';

    let texts = [];
    let errorMessage = '';
    let editText = '';
    let editId = null;

    onMount(() => {
        fetchTexts();
    });

    function fetchTexts() {
        fetch('/api/textlist/', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch texts');
            }
            return response.json();
        })
        .then(data => {
            texts = data;
        })
        .catch(error => {
            errorMessage = error.message;
        });
    }

    function handleDelete(id) {
        fetch(`/api/texts/${id}/`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to delete text');
            }
            fetchTexts();
        })
        .catch(error => {
            errorMessage = error.message;
        });
    }

    function handleEdit(id, content) {
        editId = id;
        editText = content;
    }

    function handleUpdate() {
        fetch(`/api/texts/${editId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            },
            body: JSON.stringify({ content: editText })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to update text');
            }
            editId = null;
            editText = '';
            fetchTexts();
        })
        .catch(error => {
            errorMessage = error.message;
        });
    }
</script>

<main>
    <h2>Text List</h2>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    <ul>
        {#each texts as text}
            <li>
                {#if editId === text.id}
                    <input type="text" bind:value={editText} />
                    <button on:click={handleUpdate}>Update</button>
                    <button on:click={() => { editId = null; editText = ''; }}>Cancel</button>
                {:else}
                    {text.content}
                    <button on:click={() => handleEdit(text.id, text.content)}>Edit</button>
                    <button on:click={() => handleDelete(text.id)}>Delete</button>
                {/if}
            </li>
        {/each}
    </ul>
</main>

<style>
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin: 10px 0;
        padding: 10px;
        border: 1px solid #ccc;
        display: flex;
        align-items: center;
    }
    button {
        margin-left: 10px;
    }
    input {
        flex: 1;
        margin-right: 10px;
    }
</style>
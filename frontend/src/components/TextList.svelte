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
    <div class="grid-container">
        {#each texts as text}
            <div class="grid-item">
                {#if editId === text.id}
                    <input type="text" bind:value={editText} />
                    <button on:click={handleUpdate}>Update</button>
                    <button on:click={() => { editId = null; editText = ''; }}>Cancel</button>
                {:else}
                    <div class="text-content">{text.content}</div>
                    <div class="button-container">
                        <button on:click={() => handleEdit(text.id, text.content)}>Edit</button>
                        <button on:click={() => handleDelete(text.id)}>Delete</button>
                    </div>
                {/if}
            </div>
        {/each}
    </div>
</main>

<style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 20px;
    }
    .grid-item {
        border: 1px solid #ccc;
        padding: 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .text-content {
        max-height: 100px;
        overflow-y: auto;
        margin-bottom: 10px;
    }
    .button-container {
        display: flex;
        justify-content: space-between;
    }
    input {
        margin-top: 10px;
    }
    button {
        padding: 5px 10px;
        cursor: pointer;
    }
</style>
<script>
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    import { FilmStore } from '../../film-store';

    let handleClick = () => {
        goto('/films/add/');
    }

    onMount(async () => {
        // Check if store is empty
        let films;
        FilmStore.subscribe(value => films = value)();
        if (films.length === 0) {
            const endpoint = 'http://localhost:8000/api/films/';
            try {
                let response = await fetch(endpoint);
                if (response.ok) {
                    let data = await response.json();
                    FilmStore.set(data);
                } else {
                    console.error('Failed to fetch films');
                }
            } catch (error) {
                console.error('Error fetching films:', error);
            }
        }
    });

    async function handleDelete(id) {
        // Check if store has items before attempting to delete
        let films;
        FilmStore.subscribe(value => films = value)();
        if (films.length > 0) {
            const endpoint = `http://localhost:8000/api/films/${id}/`;
            try {
                let response = await fetch(endpoint, { method: 'DELETE' });
                if (response.ok) {
                    FilmStore.update(prev => prev.filter(film => film.id !== id));
                } else {
                    console.error('Failed to delete film');
                }
            } catch (error) {
                console.error('Error deleting film:', error);
            }
        }
    }
</script>

<div>
    <h2 class="my-4">Film List</h2>
    
    <div class="my-4 row">
        {#each $FilmStore as film}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover" 
                    src="{film.image}" 
                    alt="Film">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
                    <div>
                        <h5 class="card-title">{ film.name }</h5>
                        <p class="card-text">Directed by { film.director }</p>
                    </div>
                    <div>
                        <a href="/films/{film.id}" class="btn btn-primary">View</a>
                        <button on:click={() => handleDelete(film.id)} class="btn btn-danger mx-2">Delete</button>   
                    </div>
                </div>
            </div>

        </div>
        {/each}
    </div>
    
</div>

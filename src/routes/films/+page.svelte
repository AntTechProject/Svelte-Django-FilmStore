<script>
    let films = [
        {id: 1, name: 'The GodFather', director: 'Francis'},
        {id: 2, name: 'The Batman', director: 'Nolan'},
    ]
</script>

<ul>
    {#each films as film}
        <li><a href="films/{film.id}">{film.name}</a></li>
    {/each}
</ul>
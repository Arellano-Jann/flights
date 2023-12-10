<script>
    import DataTable from "./data-table.svelte";
    
    export let data;
</script>



<div class="container mx-auto py-10">
    <DataTable flights={data.flights}/>
</div>

<style>

</style>
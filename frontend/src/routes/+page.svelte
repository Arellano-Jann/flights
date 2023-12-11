<script>
    import DataTable from "$lib/components/data-table/data-table.svelte";
    import Button from "$lib/components/ui/button/button.svelte";

    export let data;
</script>

<div class="container mx-auto py-10">
    <DataTable flights={data.flights}/>
</div>

<style>

</style>
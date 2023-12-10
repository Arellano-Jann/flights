<script>
    /** @type {import('./$types').PageData} */
    import FlightForm from '../FlightForm.svelte';
    export let data;
</script>

<FlightForm form={data.form}/>
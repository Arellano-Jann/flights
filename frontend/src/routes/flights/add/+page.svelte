<script>
    /** @type {import('./$types').PageData} */
    import FlightForm from '../FlightForm.svelte';
    import Button from "$lib/components/ui/button/button.svelte";
    import { PlaneTakeoff } from "lucide-svelte";
    export let data;
</script>
<FlightForm form={data.form}/>
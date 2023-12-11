<script>
    import { Checkbox } from "$lib/components/ui/checkbox";
    // import type {Writable} from "svelte/store";

    export let checked;
</script>

<Checkbox bind:checked={$checked}/>
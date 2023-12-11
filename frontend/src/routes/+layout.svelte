<script>
	import NavBar from "$lib/components/NavBar.svelte";
    import "../app.pcss";
    import { ModeWatcher } from "mode-watcher";
</script>

<main class="dark">
    <ModeWatcher />
    <NavBar/>
    <slot> </slot>
</main>

<style>

</style>
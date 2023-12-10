<script>
    import "../app.pcss";
    import { ModeWatcher } from "mode-watcher";
    import { Button } from "$lib/components/ui/button";
    import { Sun, Moon } from "lucide-svelte";
</script>

<main class="dark">
    <ModeWatcher />
    <slot> </slot>
</main>

<style>

</style>
<script>
    import { cn } from "$lib/utils";
    import { PlaneTakeoff, Home } from "lucide-svelte";
</script>

<div class="border-b">
    <div class="flex h-16 items-center px-4">
        <nav class={cn("flex items-center space-x-4 lg:space-x-6 mx-6")}>
            <a
                href="/"
                class="text-sm font-medium transition-colors hover:text-primary"
            >
                <Home class="mr-2 h-4 w-4"/>
            </a>
            <a
                href="/flights/add"
                class="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
            >
                <PlaneTakeoff class="mr-2 h-4 w-4"/>
            </a>
        </nav>
    </div>
</div>
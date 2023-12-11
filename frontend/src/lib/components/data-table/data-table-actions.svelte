<script>
    import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
    import Button from "$lib/components/ui/button/button.svelte";
    import { MoreHorizontal, Bomb, Pen } from "lucide-svelte";
    // import { Flights } from ;
    import { goto, invalidateAll, invalidate } from '$app/navigation';
    
    export let uuid;
    
    async function clickDelete() {
        // fetch delete
        const res = await fetch(`http://127.0.0.1:8000/backend/flights/${uuid}`, {
            method: 'DELETE'
        })
        .then(res => {
            if (res.status == 204){ // hot reloads the table
                // Flights.update(prev => prev.filter(flight => flight.uuid != uuid))
                // invalidate('http://127.0.0.1:5173/')
                invalidateAll()
            }
        })
    }
    async function clickUpdate() {
        // redirect to update
        goto(`flights/update/${uuid}`)
    }

</script>

<DropdownMenu.Root>
    <DropdownMenu.Trigger asChild let:builder>
        <Button variant="ghost" builders={[builder]} size="icon" class="relative w-8 h-8 p-0">
            <span class="sr-only">Open menu</span>
            <MoreHorizontal class="w-4 h-4"/>
        </Button>
    </DropdownMenu.Trigger>

    <DropdownMenu.Content>
        <DropdownMenu.Group>
            <DropdownMenu.Label>Actions</DropdownMenu.Label>
            <DropdownMenu.Separator />
            <DropdownMenu.Item class="text-destructive" on:click={clickDelete}>
                <Bomb class="mr-2 h-4 w-4"/> 
                Delete
            </DropdownMenu.Item>
            <DropdownMenu.Item on:click={clickUpdate}>
                <Pen class="mr-2 h-4 w-4"/> 
                Update
            </DropdownMenu.Item>
        </DropdownMenu.Group>
    </DropdownMenu.Content>

</DropdownMenu.Root>



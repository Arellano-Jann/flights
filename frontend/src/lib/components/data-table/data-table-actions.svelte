<script>
    import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
    import Button from "$lib/components/ui/button/button.svelte";
    import { MoreHorizontal } from "lucide-svelte";
    import { goto } from '$app/navigation';
    
    export let id;
    
    async function clickDelete() {
        // fetch delete
    }
    async function clickUpdate() {
        // redirect to update
        goto('flights/update/' + id)
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
            <DropdownMenu.Item on:click={clickDelete}>
                Delete
            </DropdownMenu.Item>
            <DropdownMenu.Item on:click={clickUpdate}>
                Update
            </DropdownMenu.Item>
        </DropdownMenu.Group>
    </DropdownMenu.Content>

</DropdownMenu.Root>



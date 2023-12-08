<script>
    import { createTable, Render, Subscribe, createRender } from "svelte-headless-table";
    import { addSortBy } from "svelte-headless-table/plugins";
    import { readable } from "svelte/store";
    import * as Table from "$lib/components/ui/table";
    import DataTableActions from "./data-table-actions.svelte";
    import Button from "$lib/components/ui/button/button.svelte"
    // import {Button} from "$lib/components/ui/button"
    import {ArrowUpDown} from "lucide-svelte";

    const flights = [   
        {
            "id": "m5",
            "min_cost": 1,
            "max_cost": 1,
            "from_airport": "BUR",
            "to_airport": "LAS"
        },
        {
            "id": "m6",
            "min_cost": 1,
            "max_cost": 1,
            "from_airport": "BUR",
            "to_airport": "LAS"
        }
    ];

    const table = createTable(readable(flights), {
        sort: addSortBy()
    });
    const columns = table.createColumns([
        table.column({
            accessor: "id",
            header: "ID"
        }),
        table.column({
            accessor: "min_cost",
            header: "Min Cost",
            cell: ({ value }) => {
                const formatted = new Intl.NumberFormat('en-US', {
                    style: "currency",
                    currency: "USD",
                    maximumFractionDigits: 0,
                }).format(value);
                return formatted;
            }
        }),
        table.column({
            accessor: "max_cost",
            header: "Max Cost",
            cell: ({ value }) => {
                const formatted = new Intl.NumberFormat('en-US', {
                    style: "currency",
                    currency: "USD",
                    maximumFractionDigits: 0,
                }).format(value);
                return formatted;
            }
        }),
        table.column({
            accessor: "from_airport",
            header: "Airport (Source)"
        }),
        table.column({
            accessor: "to_airport",
            header: "Airport (Dest.)"
        }),
        table.column({
            accessor: ({id}) => id,
            header: "",
            cell: ({ value }) => {
                return createRender(DataTableActions, {id: value});
            },
            plugins: {
                sort: {
                    disable: true
                }
            }
        })
    ]);

    const { headerRows, pageRows, tableAttrs, tableBodyAttrs } = table.createViewModel(columns);
</script>

<div class="rounded-md border">
    <Table.Root {...$tableAttrs}>
        <Table.Header>
            {#each $headerRows as headerRow}
                <Subscribe rowAttrs={headerRow.attrs()}>
                    <Table.Row>
                        {#each headerRow.cells as cell (cell.id)}
                            <Subscribe 
                            attrs={cell.attrs()} let:attrs 
                            props={cell.props()} let:props>
                                <Table.Head {... attrs}>
                                    <Button variant="ghost" on:click={props.sort.toggle}>
                                        {#if ["min_cost", "max_cost"].includes(cell.id)}
                                            <div class="text-right">
                                                <Render of={cell.render()}/>
                                            </div>
                                        {:else}
                                            <Render of={cell.render()}/>
                                        {/if}
                                        <ArrowUpDown class="ml-2 h-4 w-4"/>
                                    </Button>
                                </Table.Head>
                            </Subscribe>
                        {/each}
                    </Table.Row>
                </Subscribe>
            {/each}
        </Table.Header>
        <Table.Body {...$tableBodyAttrs}>
            {#each $pageRows as row (row.id)}
                <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
                    <Table.Row {...rowAttrs}>
                        {#each row.cells as cell (cell.id)}
                            <Subscribe attrs={cell.attrs()} let:attrs>
                                <Table.Cell {...attrs}>
                                    {#if ["min_cost", "max_cost"].includes(cell.id)}
                                        <div class="text-right">
                                            <Render of={cell.render()}/>
                                        </div>
                                    {:else}
                                        <Render of={cell.render()}/>
                                    {/if}
                                </Table.Cell>
                            </Subscribe>
                        {/each}
                    </Table.Row>
                </Subscribe>
            {/each}
        </Table.Body>
    </Table.Root>
</div>



<script>
    import { createTable, Render, Subscribe } from "svelte-headless-table";
    import { readable } from "svelte/store";
    import * as Table from "$lib/components/ui/table";

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

    const table = createTable(readable(flights));
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
        })
    ])

    const { headerRows, pageRows, tableAttrs, tableBodyAttrs } = table.createViewModel(columns);
</script>

<div class="rounded-md border">
    <Table.Root {...$tableAttrs}>
        <Table.Header>
            {#each $headerRows as headerRow}
                <Subscribe rowAttrs={headerRow.attrs()}>
                    <Table.Row>
                        {#each headerRow.cells as cell (cell.id)}
                            <Subscribe attrs={cell.attrs()} let:attrs props={cell.props()}>
                                <Table.Head {... attrs}>
                                    {#if ["min_cost", "max_cost"].includes(cell.id)}
                                        <div class="text-right">
                                            <Render of={cell.render()}/>
                                        </div>
                                    {:else}
                                        <Render of={cell.render()}/>
                                    {/if}
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



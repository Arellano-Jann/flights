<script>
    import { createTable, Render, Subscribe, createRender } from "svelte-headless-table";
    import { addSortBy, addTableFilter, addHiddenColumns, addSelectedRows } from "svelte-headless-table/plugins";
    import { readable } from "svelte/store";
    import DataTableActions from "./data-table-actions.svelte";
    import DataTableCheckbox from "./data-table-checkbox.svelte";
    import * as Table from "$lib/components/ui/table";
    import Button from "$lib/components/ui/button/button.svelte"
    // import {Button} from "$lib/components/ui/button"
    import { Input } from "$lib/components/ui/input";
    import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
    import {ArrowUpDown, ChevronDown} from "lucide-svelte";

    const flights = [   
        {
            "id": "m5",
            "min_cost": 1,
            "max_cost": 3,
            "from_airport": "BUR",
            "to_airport": "LAS"
        },
        {
            "id": "m6",
            "min_cost": 2,
            "max_cost": 4,
            "from_airport": "LGA",
            "to_airport": "MDW"
        }
    ];

    const table = createTable(readable(flights), {
        sort: addSortBy({ disableMultiSort: true}),
        filter: addTableFilter({
            fn: ({ filterValue, value }) =>
                value.toLowerCase().includes(filterValue.toLowerCase())
        }),
        hide: addHiddenColumns(),
        select: addSelectedRows()
    });
    const columns = table.createColumns([
        table.column({
            accessor: "id",
            header: (_, {pluginStates}) => {
                const { allPageRowsSelected } = pluginStates.select;
                return createRender(DataTableCheckbox, {
                    checked: allPageRowsSelected
                });
            },
            cell: ({row}, {pluginStates}) => {
                const { getRowState } = pluginStates.select;
                const { isSelected } = getRowState(row);

                return createRender(DataTableCheckbox, {
                    checked: isSelected
                });
            },
            plugins: {
                filter: {
                    exclude: true
                }
            }
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

    const { headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates, flatColumns, rows } = table.createViewModel(columns);
    const { filterValue } = pluginStates.filter;
    const { hiddenColumnIds } = pluginStates.hide;
    const { selectedDataIds } = pluginStates.select;

    const ids = flatColumns.map((col) => col.id);
    let hideForId = Object.fromEntries(ids.map((id) => [id, true]));

    $: $hiddenColumnIds = Object.entries(hideForId)
        .filter(([, hide]) => !hide)
        .map(([id]) => id);

    const hidableCols = ["id", "min_cost", "max_cost", "from_airport", "to_airport" ]
    
</script>


<div class="flex items-center py-4">
    <Input class="max-w-sm" placeholder="Filter" type="text" bind:value={$filterValue}/>

    <DropdownMenu.Root>
        <DropdownMenu.Trigger asChild let:builder>
            <Button variant="outline" class="ml-auto" builders={[builder]}>
                Columns <ChevronDown class="ml-2 h-4 w-4"/>
            </Button>
        </DropdownMenu.Trigger>
        <DropdownMenu.Content>
            {#each flatColumns as col}
                {#if hidableCols.includes(col.id)}
                    <DropdownMenu.CheckboxItem bind:checked={hideForId[col.id]}>
                        {col.header}
                    </DropdownMenu.CheckboxItem>
                {/if}
            {/each}
        </DropdownMenu.Content>
    </DropdownMenu.Root>
</div>

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
                                <Table.Head {... attrs} class="[&:has([role=checkbox])]:pl-3">
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
                    <Table.Row {...rowAttrs} data-state={$selectedDataIds[row.id] && "selected"}
                    >
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
<div class="flex-1 text-sm text-muted-foreground">
    {Object.keys($selectedDataIds).length} of{" "}
    {$rows.length} row(s) selected.
  </div>



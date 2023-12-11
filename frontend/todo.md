~~1. list flights (table)~~
~~4. add flight (form)~~ ~~button~~
~~2. update flight (button -> form)~~ fix sizing, popup
~~2a. delete flight (actions part)~~ active reload
3. populate data tables
3. filterFlight (filter table individually, like example)
5. graphView - graph relations of all flights - nodal
6. solve best path - (input num of destinations to visit)

- remove sort (actions) in table-data
- make column disappear if nothing inside? (maybe this is kinda handled by the hide button)

- ensure data validation (min cost < max cost) (ints) (error messages, on submit and while filling out)

- what happens in zod if some data is missing?

tool bar resources:
https://www.shadcn-svelte.com/examples/tasks
https://www.shadcn-svelte.com/docs/components/data-table#filtering
https://github.com/huntabyte/shadcn-svelte/blob/main/apps/www/src/routes/examples/tasks/(components)/data-table.svelte
https://github.com/huntabyte/shadcn-svelte/blob/main/apps/www/src/routes/examples/tasks/(components)/data-table-toolbar.svelte
https://github.com/huntabyte/shadcn-svelte/tree/main/apps/www/src/routes/examples/tasks/(components)
https://github.com/huntabyte/shadcn-svelte/blob/main/apps/www/src/routes/examples/tasks/(data)/data.ts
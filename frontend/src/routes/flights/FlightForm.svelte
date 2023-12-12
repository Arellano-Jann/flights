<script>

    // import { Form } from "$lib/components/ui/form"; // gives <Form.Root> is not a valid SSR component but idk why
    import * as Form from "$lib/components/ui/form";
    import { formSchema } from "./schema";
    // https://github.com/huntabyte/shadcn-svelte/blob/main/apps/www/src/routes/examples/forms/profile-form.svelte

    import { Calendar as CalendarIcon, Send } from "lucide-svelte";
    import {
        DateFormatter,
        getLocalTimeZone,
        parseDate,
        CalendarDate,
        today
    } from "@internationalized/date";
    import { cn } from "$lib/utils";
    import { buttonVariants } from "$lib/components/ui/button";
    import { Calendar } from "$lib/components/ui/calendar";
    import * as Popover from "$lib/components/ui/popover";
    import { superForm } from "sveltekit-superforms/client";
    export let form;

    const theForm = superForm(form, { // incoming form with validators and taints
      validators: formSchema
    });
    const { form: formStore } = theForm; // set validated form to inhouse var
    const df = new DateFormatter("en-US", { // date formatter
      dateStyle: "long"
    });
    let date_first_checked = $formStore.date_first_checked ? parseDate($formStore.date_first_checked) : undefined;
    let date_last_checked = $formStore.date_last_checked ? parseDate($formStore.date_last_checked) : undefined;
    let date_of_flight = $formStore.date_of_flight ? parseDate($formStore.date_of_flight) : undefined;
    let placeholder = today(getLocalTimeZone());

</script>

<div>
    <div class="container">
        <Form.Root method="POST" controlled form={theForm} schema={formSchema} let:config>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-x-2">
                <Form.Field {config} name="min_cost">
                    <Form.Item>
                        <Form.Label>Min Cost</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>Min cost of flight</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="max_cost">
                    <Form.Item>
                        <Form.Label>Max Cost</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>Max cost of flight</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="avg_cost">
                    <Form.Item>
                        <Form.Label>Average Cost</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>Average cost of flight (calculated automatically if empty)</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-4 gap-x-2">
                <Form.Field {config} name="from_city">
                    <Form.Item>
                        <Form.Label>City of Departure</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>City where outgoing flight takes off</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="to_city">
                    <Form.Item>
                        <Form.Label>City of Arrival</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>City where incoming flight lands</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="from_airport">
                    <Form.Item>
                        <Form.Label>Airport of Departure</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>Airport where outgoing flight takes off</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="to_airport">
                    <Form.Item>
                        <Form.Label>Airport of Arrival</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>Airport where incoming flight lands</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
            </div>
            <div class="grid grid-cols-2 gap-x-2">
                <Form.Field {config} name="airline">
                    <Form.Item>
                        <Form.Label>Airline</Form.Label>
                        <Form.Input class=""/>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="flight_code">
                    <Form.Item>
                        <Form.Label>Flight Number</Form.Label>
                        <Form.Input class=""/>
                        <Form.Description>Flight Number (i.e. DTK253)</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-4 gap-x-2"> 
                <Form.Field {config} name="date_first_checked">
                    <Form.Item>
                        <Form.Label for="date_first_checked">Price First Checked</Form.Label>
                        <Popover.Root>
                            <Form.Control id="date_first_checked" let:attrs>
                                <Popover.Trigger
                                    id="date_first_checked"
                                    {...attrs}
                                    class={cn(
                                    buttonVariants({ variant: "outline" }),
                                    "w-full pl-4 justify-start text-left font-normal",
                                    !date_first_checked && "text-muted-foreground"
                                    )}
                                >
                                    {date_first_checked
                                    ? df.format(date_first_checked.toDate(getLocalTimeZone()))
                                    : "Pick a date"}
                                    <CalendarIcon class="ml-auto h-4 w-4 opacity-50" />
                                </Popover.Trigger>
                            </Form.Control>
                            <Popover.Content class="w-auto p-0" side="top">
                                <Calendar
                                    bind:value={date_first_checked}
                                    bind:placeholder
                                    minValue={new CalendarDate(1900, 1, 1)}
                                    maxValue={today(getLocalTimeZone())}
                                    calendarLabel="date_first_checked"
                                    initialFocus
                                    onValueChange={(v) => {
                                        if (v) {
                                            $formStore.date_first_checked = v.toString();
                                        } else {
                                            $formStore.date_first_checked = "";
                                        }
                                    }}
                                />
                            </Popover.Content>
                        </Popover.Root>
                        <Form.Description>Date the flight price was first checked</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="date_last_checked">
                    <Form.Item>
                        <Form.Label>Price Last Checked</Form.Label>
                        <Popover.Root>
                            <Form.Control id="date_last_checked" let:attrs>
                                <Popover.Trigger
                                    id="date_last_checked"
                                    {...attrs}
                                    class={cn(
                                    buttonVariants({ variant: "outline" }),
                                    "w-full pl-4 justify-start text-left font-normal",
                                    !date_last_checked && "text-muted-foreground"
                                    )}
                                >
                                    {date_last_checked
                                    ? df.format(date_last_checked.toDate(getLocalTimeZone()))
                                    : "Pick a date"}
                                    <CalendarIcon class="ml-auto h-4 w-4 opacity-50" />
                                </Popover.Trigger>
                            </Form.Control>
                            <Popover.Content class="w-auto p-0" side="top">
                                <Calendar
                                    bind:value={date_last_checked}
                                    bind:placeholder
                                    minValue={new CalendarDate(1900, 1, 1)}
                                    maxValue={today(getLocalTimeZone())}
                                    calendarLabel="date_last_checked"
                                    initialFocus
                                    onValueChange={(v) => {
                                        if (v) {
                                            $formStore.date_last_checked = v.toString();
                                        } else {
                                            $formStore.date_last_checked = "";
                                        }
                                    }}
                                />
                            </Popover.Content>
                        </Popover.Root>
                        <Form.Description>Date the flight price was last checked</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="date_of_flight">
                    <Form.Item>
                        <Form.Label>Date of Flight</Form.Label>
                        <Popover.Root>
                            <Form.Control id="date_of_flight" let:attrs>
                                <Popover.Trigger
                                    id="date_of_flight"
                                    {...attrs}
                                    class={cn(
                                    buttonVariants({ variant: "outline" }),
                                    "w-full pl-4 justify-start text-left font-normal",
                                    !date_of_flight && "text-muted-foreground"
                                    )}
                                >
                                    {date_of_flight
                                    ? df.format(date_of_flight.toDate(getLocalTimeZone()))
                                    : "Pick a date"}
                                    <CalendarIcon class="ml-auto h-4 w-4 opacity-50" />
                                </Popover.Trigger>
                            </Form.Control>
                            <Popover.Content class="w-auto p-0" side="top">
                                <Calendar
                                    bind:value={date_of_flight}
                                    bind:placeholder
                                    minValue={new CalendarDate(1900, 1, 1)}
                                    calendarLabel="date_of_flight"
                                    initialFocus
                                    onValueChange={(v) => {
                                        if (v) {
                                            $formStore.date_of_flight = v.toString();
                                        } else {
                                            $formStore.date_of_flight = "";
                                        }
                                    }}
                                />
                            </Popover.Content>
                        </Popover.Root>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
                <Form.Field {config} name="day_of_flight">
                    <Form.Item>
                        <Form.Label>Day of Flight</Form.Label>
                        <Form.Select>
                            <Form.SelectTrigger
                                placeholder="Select a day of the week"
                            />
                            <Form.SelectContent>
                                <Form.SelectItem value="Monday" label="Monday"
                                    >Monday
                                </Form.SelectItem>
                                <Form.SelectItem value="Tuesday" label="Tuesday"
                                    >Tuesday
                                </Form.SelectItem>
                                <Form.SelectItem value="Wednesday" label="Wednesday"
                                    >Wednesday
                                </Form.SelectItem>
                                <Form.SelectItem value="Thursday" label="Thursday"
                                    >Thursday
                                </Form.SelectItem>
                                <Form.SelectItem value="Friday" label="Friday"
                                    >Friday
                                </Form.SelectItem>
                                <Form.SelectItem value="Saturday" label="Saturday"
                                    >Saturday
                                </Form.SelectItem>
                                <Form.SelectItem value="Sunday" label="Sunday"
                                    >Sunday
                                </Form.SelectItem>
                            </Form.SelectContent>
                        </Form.Select>
                        <Form.Description>Day of Flight</Form.Description>
                        <Form.Validation/>
                    </Form.Item>
                </Form.Field>
            </div>
            <Form.Button>
                <Send class="ml-auto mr-2 h-4 w-4" />
                Submit
            </Form.Button>
        </Form.Root>
    </div>
</div>

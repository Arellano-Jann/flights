<script>
    import DatePicker from "$lib/components/date-picker/DatePicker.svelte";

    // import { Form } from "$lib/components/ui/form"; // gives <Form.Root> is not a valid SSR component but idk why
    import * as Form from "$lib/components/ui/form";
    import { formSchema } from "./schema";
    // https://github.com/huntabyte/shadcn-svelte/blob/main/apps/www/src/routes/examples/forms/profile-form.svelte

    
    import { Calendar as CalendarIcon } from "lucide-svelte";
    import {
        DateFormatter,
        getLocalTimeZone,
        parseDate,
        CalendarDate,
        today
    } from "@internationalized/date";
    import { cn } from "$lib/utils";
    import { Button, buttonVariants } from "$lib/components/ui/button";
    import { Calendar } from "$lib/components/ui/calendar";
    import * as Popover from "$lib/components/ui/popover";
    import { superForm } from "sveltekit-superforms/client";
    export let form;

    const theForm = superForm(form, { // incoming form with validators and taints
      validators: formSchema,
      taintedMessage: null
    });
    const { form: formStore } = theForm; // set validated form to inhouse var
    const df = new DateFormatter("en-US", { // date formatter
      dateStyle: "long"
    });
    let value = $formStore.date_of_flight;
    let placeholder = today(getLocalTimeZone());

</script>

<DatePicker/>

<Form.Root method="POST" {form} schema={formSchema} let:config>
    <Form.Field {config} name="min_cost">
        <Form.Item>
            <Form.Label>min_cost</Form.Label>
            <Form.Input>placeholder</Form.Input>
            <Form.Description>min_cost</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="max_cost">
        <Form.Item>
            <Form.Label>max_cost</Form.Label>
            <Form.Input/>
            <Form.Description>max_cost</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="avg_cost">
        <Form.Item>
            <Form.Label>avg_cost</Form.Label>
            <Form.Input/>
            <Form.Description>avg_cost</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="from_city">
        <Form.Item>
            <Form.Label>from_city</Form.Label>
            <Form.Input/>
            <Form.Description>from_city</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="to_city">
        <Form.Item>
            <Form.Label>to_city</Form.Label>
            <Form.Input/>
            <Form.Description>to_city</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="from_airport">
        <Form.Item>
            <Form.Label>from_airport</Form.Label>
            <Form.Input/>
            <Form.Description>from_airport</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="to_airport">
        <Form.Item>
            <Form.Label>to_airport</Form.Label>
            <Form.Input/>
            <Form.Description>to_airport</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="airline">
        <Form.Item>
            <Form.Label>airline</Form.Label>
            <Form.Input/>
            <Form.Description>airline</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="flight_code">
        <Form.Item>
            <Form.Label>flight_code</Form.Label>
            <Form.Input/>
            <Form.Description>flight_code</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="date_first_checked">
        <Form.Item>
            <Form.Label>date_first_checked</Form.Label>
            <Popover.Root>
                <Form.Control id="date" let:attrs>
                  <Popover.Trigger
                    id="date"
                    {...attrs}
                    class={cn(
                      buttonVariants({ variant: "default" }),
                      "w-[280px] pl-4 justify-start text-left font-normal",
                      !value && "text-muted-foreground"
                    )}
                  >
                    {value
                      ? df.format(value.toDate(getLocalTimeZone()))
                      : "Pick a date"}
                    <CalendarIcon class="ml-auto h-4 w-4 opacity-50" />
                  </Popover.Trigger>
                </Form.Control>
                <Popover.Content class="w-auto p-0" side="top">
                  <Calendar
                    bind:value
                    bind:placeholder
                    minValue={new CalendarDate(1900, 1, 1)}
                    maxValue={today(getLocalTimeZone())}
                    calendarLabel="Date of birth"
                    initialFocus
                    onValueChange={(v) => {
                      if (v) {
                        $formStore.date_first_checked = parseDate(v.toString());
                      } else {
                        $formStore.date_first_checked = "";
                      }
                    }}
                  />
                </Popover.Content>
              </Popover.Root>
            <Form.Description>date_first_checked</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="date_last_checked">
        <Form.Item>
            <Form.Label>date_last_checked</Form.Label>
            <Form.Input/>
            <Form.Description>date_last_checked</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="date_of_flight">
        <Form.Item>
            <Form.Label>date_of_flight</Form.Label>
            <Form.Input/>
            <Form.Description>date_of_flight</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Field {config} name="day_of_flight">
        <Form.Item>
            <Form.Label>day_of_flight</Form.Label>
            <Form.Input/>
            <Form.Description>day_of_flight</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>


    <!-- <Form.Item>
        <Form.Field {config} name="email">
            <Form.Label>Email</Form.Label>
            <Form.Select>
                <Form.SelectTrigger
                    placeholder="Select a verified email to display"
                />
                <Form.SelectContent>
                    <Form.SelectItem value="m@example.com" label="m@example.com"
                        >m@example.com
                    </Form.SelectItem>
                    <Form.SelectItem value="m@google.com" label="m@google.com"
                        >m@google.com
                    </Form.SelectItem>
                    <Form.SelectItem value="m@support.com" label="m@support.com"
                        >m@support.com
                    </Form.SelectItem>
                </Form.SelectContent>
            </Form.Select>
            <Form.Description>
                You can manage verified email addresses in your <a
                    href="/examples/forms">email settings</a
                >.
            </Form.Description>
            <Form.Validation />
        </Form.Field>
    </Form.Item> -->

    <Form.Button>Submit</Form.Button>
</Form.Root>

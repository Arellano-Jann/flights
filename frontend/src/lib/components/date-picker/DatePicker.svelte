<script lang="ts">
  import { formSchema, type FormSchema } from "./schema";
  import * as Form from "$lib/components/ui/form";
  import type { SuperValidated } from "sveltekit-superforms";

    import { page } from "$app/stores";
    import { Calendar as CalendarIcon } from "lucide-svelte";
    import {
      type DateValue,
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
    export let form: SuperValidated<FormSchema> = $page.data.datePicker;
  
    const theForm = superForm(form, { // incoming form with validators and taints
      validators: formSchema,
      taintedMessage: null
    });
  
    const { form: formStore } = theForm; // set validated form to inhouse var
  
    const df = new DateFormatter("en-US", { // date formatter
      dateStyle: "long"
    });
  
    let value: DateValue | undefined = $formStore.date_of_flight // formStores parsed datevalue
      ? parseDate($formStore.date_of_flight)
      : undefined;
  
    let placeholder: DateValue = today(getLocalTimeZone()); // highlighted day
  </script>
  
  <Form.Root
    schema={formSchema}
    controlled
    form={theForm}
    let:config
    class="space-y-8"
  >
    <Form.Field {config} name="date_of_flight">
      <Form.Item class="flex flex-col">
        <Form.Label for="date_of_flight">date_of_flight</Form.Label>
        <Popover.Root>
          <Form.Control id="date" let:attrs>
            <Popover.Trigger
              id="date"
              {...attrs}
              class={cn(
                buttonVariants({ variant: "outline" }),
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
                  $formStore.date_of_flight = v.toString();
                } else {
                  $formStore.date_of_flight = "";
                }
              }}
            />
          </Popover.Content>
        </Popover.Root>
        <Form.Description> date_of_flight</Form.Description>
        <Form.Validation />
      </Form.Item>
    </Form.Field>
    <Button type="submit">Submit</Button>
  </Form.Root>
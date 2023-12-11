<script>
	// import { Form } from "$lib/components/ui/form"; // gives <Form.Root> is not a valid SSR component but idk why
	import * as Form from "$lib/components/ui/form";
    import { formSchema } from "./schema";
    // https://github.com/huntabyte/shadcn-svelte/blob/main/apps/www/src/routes/examples/forms/profile-form.svelte

    export let form;
</script>

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

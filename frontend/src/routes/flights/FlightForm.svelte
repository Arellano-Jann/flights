<script>
	import { Form } from "$lib/components/ui/form";
    import { formSchema } from "./schema";

    export let form;
</script>

<Form.Root method="POST" {form} schema={formSchema} let:config>
    <Form.Field {config} name="username">
        <Form.Item>
            <Form.Label>Label</Form.Label>
            <Form.Input/>
            <Form.Description>Description</Form.Description>
            <Form.Validation/>
        </Form.Item>
    </Form.Field>
    <Form.Button>Submit</Form.Button>
</Form.Root>
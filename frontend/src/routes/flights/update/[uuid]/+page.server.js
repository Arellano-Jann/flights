/** @type {import('../$types').PageLoad} */
import { superValidate } from "sveltekit-superforms/server";
import { formSchema } from "../../schema";
import { fail } from "@sveltejs/kit";

export async function load({params}) {
    const res = await fetch(`http://127.0.0.1:8000/backend/flights/${params.uuid}`, {
        headers: {
            "Content-Type": "application/json"
        },
        method: 'GET'
    });
    
    const flight = await res.json();
    console.log("Individual Flight:", JSON.stringify(flight));
    return {
        uuid: params.uuid,
        flight: flight,
        form: superValidate(formSchema) // possible typescript shit
    };
};

export const actions = {
    default: async ({params, request}) => {
      const form = await superValidate(request, formSchema);
      if (!form.valid) {
        return fail(400, {
          form
        });
      }
      console.log("PATCH", form.data)
      const res = await fetch(`http://127.0.0.1:8000/backend/flights/${params.uuid}/`, {
        method: 'PATCH',
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form.data)
      })
        
      const json = await res.json();
      console.log("Return PATCH", JSON.stringify(json));
    }
  };

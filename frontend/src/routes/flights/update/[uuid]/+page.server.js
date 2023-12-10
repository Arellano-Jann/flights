/** @type {import('../$types').PageLoad} */
import { superValidate } from "sveltekit-superforms/server";
import { formSchema } from "../../schema";
import { fail } from "@sveltejs/kit";

export async function load() {
    return {
        form: superValidate(formSchema) // possible typescript shit
    };
};

export const actions = {
    default: async (event) => {
      const form = await superValidate(event, formSchema);
      if (!form.valid) {
        return fail(400, {
          form
        });
      }
      console.log(form.data)
      const res = await fetch('http://127.0.0.1:8000/backend/flights/', {
        method: 'POST',
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form.data)
      })
        
      const json = await res.json();
      console.log(JSON.stringify(json));
    }
  };
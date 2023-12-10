/** @type {import('./$types').PageLoad} */
import { superValidate } from "sveltekit-superforms/server";
import { formSchema } from "../schema";
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
      return {
        form
      };
    }
  };
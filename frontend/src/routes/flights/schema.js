import { z } from "zod";

export const formSchema = z.object({
    min_cost: z.coerce.number().nullish().default(),
    // min_cost: z.coerce.number().nonnegative().int().finite().safe(),
    max_cost: z.coerce.number().nonnegative().int().finite().safe().nullish().default(),
    avg_cost: z.coerce.number().nonnegative().finite().safe().nullish().default(),
    from_city: z.string(),
    to_city: z.string(),
    from_airport: z.string().toUpperCase().max(3).nullish().default(),
    to_airport: z.string().toUpperCase().max(3).nullish().default(),
    airline: z.string(),
    flight_code: z.string(),
    date_first_checked: z.string().nullish().or(z.string().max(0)),
    date_last_checked: z.string().nullish().or(z.string().max(0)),
    date_of_flight: z.string().nullish().or(z.string().max(0)),
    day_of_flight: z.string().max(9)
});
import { z } from "zod";

export const formSchema = z.object({
    min_cost: z.coerce.number().nonnegative().int().finite().safe(),
    max_cost: z.coerce.number().nonnegative().int().finite().safe(),
    avg_cost: z.coerce.number().nonnegative().finite().safe(),
    from_city: z.string(),
    to_city: z.string(),
    from_airport: z.string().toUpperCase().max(3),
    to_airport: z.string().toUpperCase().max(3),
    airline: z.string(),
    flight_code: z.string(),
    date_first_checked: z.string(),
    date_last_checked: z.string(),
    date_of_flight: z.string(),
    day_of_flight: z.string().max(9)
});
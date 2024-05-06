# flights

Get docker compose and then
`make docker_compose_up`
backend.localhost is the intended frontend for this project currently

WRITE A SCRIPT TO BACKFILL IF DATA ISN'T FILLED YET

on any one day, there exists a price for a flight on another day that is about the same yearly (minus volatility, demand, stock)
thus if we collect the price of a flight on day X when we try to book on day Y (about Y-X days before), and build a history out of that, we can predict when to best book a flight

obviously, what matters is what flight we can book right now so we give u places to layover for an unspecified time before going to your final destination
this is particularly useful if u wanna vacation in mutiple places before the final destination
for example, it might take $700 to go to the netherlands but... it would take $150 to go to athens and another $100 to go to the netherlands from athens, provided you stay in athens for more than a day.
this is mostly targeted towards young people with no restrictions.
there's also the fact that if there's price protection, there is no reason not to book a flight instantly.
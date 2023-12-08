<script>
    import DataTable from "./data-table.svelte";

    let min_cost = "t"
    let max_cost = "t"
    let from_airport = "t"
    let to_airport = "t"
    let flight_form = {
        "min_cost": 1,
        "max_cost": 1,
        "from_airport": "BUR",
        "to_airport": "LAS"
    }
    
    
    
    async function doPost(){
        const res = await fetch('http://127.0.0.1:8000/flights/flights/', {
            method: 'POST',
            mode: "cors",
            headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: JSON.stringify(flight_form)
        })
        
        const json = await res.json();
        console.log(JSON.stringify(json));
    }

</script>



<div class="container mx-auto py-10">
    <DataTable/>
</div>

<style>

</style>
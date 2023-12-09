<script>
    import DataTable from "./data-table.svelte";

    let min_cost = ""
    let max_cost = ""
    let from_airport = ""
    let to_airport = ""

    let flight_form = {
        "min_cost": 1,
        "max_cost": 1,
        "from_airport": "BUR",
        "to_airport": "LAS"
    }
    
    
    // async function doPost(){
    //     const res = await fetch('http://127.0.0.1:8000/flights/flights/', {
    //         method: 'POST',
    //         mode: "cors",
    //         headers: {
    //             "Content-Type": "application/json",
    //             // 'Content-Type': 'application/x-www-form-urlencoded',
    //         },
    //         body: JSON.stringify(flight_form)
    //     })
        
    //     const json = await res.json();
    //     console.log(JSON.stringify(json));
    // }
    
    export let data;
</script>



<div class="container mx-auto py-10">
    <DataTable flights={data.flights}/>
</div>

<style>

</style>
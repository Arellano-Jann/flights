/** @type {import('./$types').PageLoad} */
export async function load() {

    const res = await fetch('http://127.0.0.1:8000/backend/flights/', {
        headers: {
            "Content-Type": "application/json"
        },
        method: 'GET'
    });
    
    const flights = await res.json();
    console.log(JSON.stringify(flights));
    // async function getTableData(){
    //     const res = await fetch('http://127.0.0.1:8000/backend/flights/', {
    //         headers: {
    //             "Content-Type": "application/json"
    //         },
    //         method: 'GET'
    //     })
        
    //     const json = await res.json();
    //     console.log(JSON.stringify(json));
    // };

    // let flights = [   
    //     {
    //         "id": "m5",
    //         "min_cost": 1,
    //         "max_cost": 3,
    //         "from_airport": "BUR",
    //         "to_airport": "LAS"
    //     },
    //     {
    //         "id": "m6",
    //         "min_cost": 2,
    //         "max_cost": 4,
    //         "from_airport": "LGA",
    //         "to_airport": "MDW"
    //     }
    // ];
    
    return { flights };
};
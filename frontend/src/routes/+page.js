/** @type {import('./$types').PageLoad} */
export async function load() {

    const res = await fetch('http://backend.localhost/backend/flights/', {
        headers: {
            "Content-Type": "application/json"
        },
        method: 'GET'
    });
    
    const flights = await res.json();
    console.log("GET TABLE", JSON.stringify(flights));
    
    return { flights };
};
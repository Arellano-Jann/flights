/** @type {import('./$types').PageLoad} */
export async function load() {

    const res = await fetch('http://127.0.0.1:8000/backend/flights/', {
        headers: {
            "Content-Type": "application/json"
        },
        method: 'GET'
    });
    
    const flights = await res.json();
    console.log("GET TABLE", JSON.stringify(flights));
    
    return { flights };
};
<script>
let target = "t"
    let protocol = "t"
    let args = "t"
    let task_form = {
        "start_time": null,
        "end_time": null,
        "in_progress": false,
        "data": "",
        "user": null,
        "endpoint": null
    }
    
    
    async function doPost(){
        // let body = JSON.stringify(
        //     {
        //         "target": target,
        //         "protocol": protocol,
        //         "args": args,
        //         "xxx": "xxx"
        //     }
        // );
        let body = {
                "target": target,
                "protocol": protocol,
                "args": args,
                "xxx": "xxx"
            }
        const res = await fetch('http://127.0.0.1:8000/backend/credentials/', {
            method: 'POST',
            mode: "cors",
            headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: JSON.stringify(
                {
                    "credential_type": "test",
                    "credential_value": body,
                    "expiry": null,
                    "task": null
                }
            )
        })
        
        const json = await res.json();
        console.log(JSON.stringify(json));
    }

</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<style>

</style>
import type { PageServerLoad } from './$types';

const route = "http://localhost:8000/api/v1/contratos"

export const load: PageServerLoad = async ({ fetch }) => {
    const response = await fetch(route);
    const data = await response.json();
    console.log(data)
    return {
        contratos: data
    };
}

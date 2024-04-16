import { FilterValues, DashboardTile } from './types'

/**
 * Returns array of all DashboardTiles
 */
export async function getAllDashboardTiles(): Promise<DashboardTile[]> {
    const data = await fetch(`http://127.0.0.1:8000/oracle_connection/dashboard/`);

    return await data.json();
}

/**
 * 
 * @param id of DashboardTile to fetch
 * @returns Dashboard Tile object with specified id
 */
export async function getDashboardTileById(id: String): Promise<DashboardTile | undefined> {
    const data = await fetch(`http://127.0.0.1:8000/oracle_connection/dashboard/?tile=${id}`);

    return await data.json();
}

export async function getAllFilteredTiles(filters: FilterValues) {
    return (await fetch("http://127.0.0.1:8000/oracle_connection/tuna/", {
        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify(filters)
    })).json();
}

export async function getFilteredDataForTileById(filters: FilterValues, id: string) {
    return (await fetch(`http://127.0.0.1:8000/oracle_connection/dashboard/${id}`, {
        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify(filters)
    })).json();
}
export async function getTupleCount(): Promise<number> {

    const res = await fetch('http://127.0.0.1:8000/oracle_connection/schneider');
    const tupleCount = await res.json();

    return tupleCount[0].totalCount;
}

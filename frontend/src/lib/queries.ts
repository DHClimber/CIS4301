import { DashboardTile } from './types'
import { testTiles } from '@/app/test-data';

/**
 * Returns array of all DashboardTiles
 */
export async function getAllDashboardTiles(minDate: string, maxDate: string): Promise<DashboardTile[] | null> {
    
    const data = await fetch(`http://127.0.0.1:8000/oracle_connection/dashboard/?minDate=${minDate}&maxDate=${maxDate}`);
    const testTiles = await data.json();

    return testTiles;
}

/**
 * 
 * @param id of DashboardTile to fetch
 * @returns Dashboard Tile object with specified id
 */
export async function getDashboardTileById(id: string): Promise<DashboardTile | undefined> {
    
    const data = await fetch(`http://127.0.0.1:8000/oracle_connection/dashboard/?tile=${id}`);
    const testTile = await data.json();

    return testTile;
}

export async function getTupleCount(): Promise<number> {

    const res = await fetch('http://127.0.0.1:8000/oracle_connection/schneider');
    const tupleCount = await res.json();

    return tupleCount.totalCount;
}
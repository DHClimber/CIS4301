import { DashboardTile } from './types'
import { testTiles } from '@/app/test-data';

/**
 * Returns array of all DashboardTiles
 */
export async function getAllDashboardTiles(): Promise<DashboardTile[] | null> {
    
    const data = await fetch("http://127.0.0.1:8000/oracle_connection/dashboard/");
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



//---- in django
// const queryMap = {
//     [id: string]: string;
// }

// {"1": "Select * from Crashes", "2": "Select * from People"}

// let query = queryMap[req.query.tile];

// let minDate = '1-2-2024'; // constraint

// query = query + ` where Crash_date > ${minDate}`;

// // call oracle sql qith "query" variable


import { DashboardTile } from './types'
import { testTiles } from '@/app/test-data';

/**
 * Returns array of all DashboardTiles
 */
export async function getAllDashboardTiles(): Promise<DashboardTile[] | null> {
    // return djangoQueries.fetch('/dashboardTiles') => returns array of all dashboard tiles
    return testTiles;
}

/**
 * 
 * @param id of DashboardTile to fetch
 * @returns Dashboard Tile object with specified id
 */
export function getDashboardTileById(id: string): DashboardTile | undefined {
    // return djangoQueries.get(/dashboardTile/[id]) => returns dashboard tile object with that id
    return testTiles.find((tile) => tile.id === id);
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


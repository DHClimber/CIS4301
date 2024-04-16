import { BarChartDataFormat, DashboardTile } from "./types";

export function formatDate(date: Date | string) {
    if (typeof date === "string") {
        let dateTypeDate = new Date(date);
        const offset = dateTypeDate.getTimezoneOffset()
        dateTypeDate = new Date(dateTypeDate.getTime() - (offset*60*1000))
        return dateTypeDate.toISOString().split('T')[0]
    }
    const offset = date.getTimezoneOffset()
    date = new Date(date.getTime() - (offset*60*1000))
    return date.toISOString().split('T')[0]
}

export function generateHexColorFromLetter (seed: number) {
    let color = Math.floor((Math.abs(Math.sin(seed) * 16777215))).toString(16);
    // pad any colors shorter than 6 characters with leading 0s
    while(color.length < 6) {
      color = '0' + color;
    }
  
    return color;
  }

export const getKeysForData = (data: BarChartDataFormat[]) => {
    const keys = new Set<string>();
    data.forEach((d) => {
      Object.keys(d).forEach((key) => {
        if (key !== "name") {
            keys.add(key);
        }
      });
    });
    return Array.from(keys);
};

export const getIdToKeysMap = (newTiles: DashboardTile[]) => {
    const idToKeysMap: {[id: string]: string[]} = {};
    newTiles.forEach((tile) => {
        idToKeysMap[tile.id] = getKeysForData(tile.data);
    });
    return idToKeysMap;
}
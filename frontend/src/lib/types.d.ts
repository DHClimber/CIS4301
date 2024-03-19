export type BarChartData = {
    name: string,
    uv: number,
    pv: number,
    amt: number,
}

export type DashboardTile = {
    id: string; // corresponds to id in DB
    title: string; // name of data it's representing ex "Crashes per year"
    data: BarChartData[] // JSON format of data returned
}

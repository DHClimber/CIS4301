// export type BarChartDataFormat = {
//     xAxisValue: number;
//     yAxisValue: number;
// }

export type DashboardTile = {
    id: string; // corresponds to id in DB
    title: string; // name of data it's representing ex "Crashes per year"
    xAxisLabel: string;
    yAxisLabel: string;
    data: BarChartData[] // JSON format of data returned
}

export type BarChartDataFormat = {
    [xAxisValue: string]: number;
    [yAxisValue: string]: number;
}
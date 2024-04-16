export type DashboardTile = {
    id: string; // corresponds to id in DB
    title: string; // name of data it's representing (ex "Crashes per year")
    xAxisLabel: string; // Label for whole x-axis (ex "Year")
    yAxisLabel: string; // Label for whole y-axis (ex "Number of Crashes")
    data: BarChartDataFormat[] // Format of data returned from DB
}

export type BarChartDataFormat = {
    'name': string;
    [yAxisKey: string]: number;
}

export type FilterProps = {
    datePicker?: true;
    sexSelect?: true;
    ageRange?: true;
    weather?: true;
    onSubmit: (filters: FilterValues) => void;
}

export type FilterValues = {
    view?: string;
    datePicker?: number[];
    sexSelect?: string;
    ageRange?: number[];
    weather?: string[];
}
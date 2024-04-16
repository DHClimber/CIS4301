"use client"
import { formatDate } from "@/lib/functions";
import { FilterProps as FilterControlsProps } from "@/lib/types";
import { Autocomplete, Box, Button, Card, Chip, Divider, FormControlLabel, FormGroup, Input, Radio, RadioGroup, Slider, Stack, TextField, Typography } from "@mui/material";
import { useState } from "react";

const weatherOptions = [
    'FOG/SMOKE/HAZE',
    'SEVERE CROSS WIND GATE',
    'SNOW',
    'OTHER',
    'CLEAR',
    'RAIN',
    'CLOUDY/OVERCAST',
    'UNKNOWN',
    'SLEET/HAIL'
]

export default function FilterControls(props: FilterControlsProps) {
    const [startDate, setStartDate] = useState<string>("");
    const [endDate, setEndDate] = useState<string>("");
    const [sex, setSex] = useState<string>("ALL");
    const [ageRange, setAgeRange] = useState<number[]>([0, 120]);
    const [weather, setWeather] = useState<string[]>([]);
    const [error, setError] = useState<string>();

    const handleAgeRangeChange = (event: Event, newValue: number | number[]) => {
        setAgeRange(newValue as number[]);
    };

    const ageRangeLabels = [{value: 0, label: '0'}, {value: 120, label: '120'}];

    function handleSubmit() {
        if (new Date(startDate) > new Date(endDate)) {
            setError("Start date must be before end date");
            return;
        } else if (startDate && !endDate || !startDate && endDate) {
            setError("Needs both or neither dates");
            return;
        }
        setError("");
        const filters = {
            ...(startDate && endDate ? {dates: [formatDate(startDate), formatDate(endDate)]} : {dates : ["", ""]}),
            ...(sex ? {sex: sex} : {sex : "ALL"}),
            ...(ageRange ? {ageRange: ageRange} : {ageRange : [0, 120]}),
            ...(weather.length ? {weather: weather} : {weather : []}),
        }
        console.log("Sending data: ", filters);
        props.onSubmit(filters);    
    }

    return (
        <Card sx={{padding: 4}}>
            <FormGroup>
                <Stack gap={2}>
                    <Typography variant='h5'>Controls</Typography>
                    <Divider />
                    <Box display={{display: props.datePicker ? 'block' : 'none'}}>
                        <Typography variant='h6'>Date Range</Typography>
                        <Input 
                            type='date' 
                            onChange={(e) => setStartDate(e.target.value)}
                            value={startDate}
                        />
                        to &nbsp;
                        <Input
                            type='date' 
                            onChange={(e) => setEndDate(e.target.value)}
                            value={endDate}
                        />
                    </Box>
                    <Box display={{display: props.sexSelect ? 'block' : 'none'}}>
                        <Typography variant='h6'>Sex</Typography>
                        <RadioGroup 
                            sx={{display: "flex", flexDirection: "row"}}
                            value={sex} 
                            onChange={(e, newVal) => setSex(newVal)}
                        >
                            <FormControlLabel value="F" control={<Radio />} label="Female" />
                            <FormControlLabel value="M" control={<Radio />} label="Male" />
                            <FormControlLabel value="ALL" control={<Radio />} label="All" />
                        </RadioGroup>
                    </Box>
                    <Box display={{display: props.ageRange ? 'block' : 'none'}}>
                        <Typography variant='h6'>Age Range</Typography>
                        <Slider
                            value={ageRange}
                            onChange={handleAgeRangeChange}
                            valueLabelDisplay="auto"
                            marks={ageRangeLabels}
                            max={120}
                        />
                    </Box>
                    <Box display={{display: props.weather ? 'block' : 'none'}}>
                        <Typography variant='h6'>Weather</Typography>
                        <Autocomplete
                            multiple
                            disablePortal
                            id="combo-box-demo"
                            options={weatherOptions}
                            sx={{ width: 300 }}
                            value={weather}
                            onChange={(e, newVal) => {
                                setWeather(newVal)
                            }}
                            renderInput={(params) => 
                                <TextField {...params} placeholder={weather.length === 0 ? "Start typing or select" : ""} />
                            }
                            renderTags={(tagValue, getTagProps) =>
                                tagValue.map((option, index) => (
                                    <Chip label={option} {...getTagProps({ index })} />
                                ))
                            }
                        />
                    </Box>
                    <Button variant="contained" onClick={handleSubmit}>Submit</Button>
                    {error && 
                        <Box style={{color: "red"}}>
                            Error: {error}
                        </Box>
                    }
                </Stack>
            </FormGroup>
        </Card>
    );
}




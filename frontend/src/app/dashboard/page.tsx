'use client'
import { getAllDashboardTiles, getAllFilteredTiles } from '@/lib/queries';
import { Button, Card, CircularProgress, Grid, Link, Stack, Typography } from '@mui/material'
import { Bar, BarChart, ResponsiveContainer, XAxis, YAxis } from 'recharts';
import FilterControls from '@/components/shared/filter-controls';
import { FilterValues, DashboardTile, BarChartDataFormat } from '@/lib/types';
import { useEffect, useState } from 'react';
import { generateHexColorFromLetter, getIdToKeysMap } from '@/lib/functions';

export default function Dashboard() {
  const [tiles, setTiles] = useState<DashboardTile[]>([]);
  const [tileIdToChartKeys, setTileIdToChartKeys] = useState<{[id: string]: string[]}>();

  useEffect(() => {
    (async () => {
      const dashTiles: DashboardTile[] = await getAllDashboardTiles() || [];
      setTiles(dashTiles);
      setTileIdToChartKeys(getIdToKeysMap(dashTiles));
    })(); 
  }, []);

  const onFiltersSubmit = async (filters: FilterValues) => {
    const newDashTiles = await getAllFilteredTiles(filters);
    setTiles(newDashTiles);
    getIdToKeysMap(newDashTiles);
  }

  return (
    <Stack spacing={1}>
      <Typography variant='h3'>Dashboard</Typography>
      <Stack direction={'row'} gap={2}>
        <Grid container spacing={1}>
          {tileIdToChartKeys ? tiles.map((tile) => (
            <Grid item xs={6}>
              <Card sx={{padding: 5}}>
                <Typography variant='h6'>{tile.title}</Typography>            
                <ResponsiveContainer width={250} height={150}>
                  <BarChart width={250} height={150} data={tile.data}>
                    <XAxis dataKey="YEAR" angle={-45}/>
                    <YAxis />
                    {tileIdToChartKeys[tile.id].map((key: string) => {
                      const color = generateHexColorFromLetter(key.charCodeAt(0));
                      return <Bar dataKey={key} fill={`#${color}`} />
                    })}
                  </BarChart>
                </ResponsiveContainer>
                <Link href={`/dashboard/${tile.id}`}>
                  <Button>See more</Button>
                </Link>
              </Card>
            </Grid>
          )) : (
            <CircularProgress />
          )}
        </Grid>
        <FilterControls datePicker onSubmit={onFiltersSubmit}/>
      </Stack>
    </Stack>
  )
}
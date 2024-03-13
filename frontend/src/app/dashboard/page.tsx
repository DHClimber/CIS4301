'use client'
import { DashboardTile } from '@/lib/types'
import { Button, Card, Grid, Stack, Typography } from '@mui/material'
import { Bar, BarChart, ResponsiveContainer } from 'recharts';

const data = [
  {
    name: 'Page A',
    uv: 4000,
    pv: 2400,
    amt: 2400,
  },
  {
    name: 'Page B',
    uv: 3000,
    pv: 1398,
    amt: 2210,
  },
  {
    name: 'Page C',
    uv: 2000,
    pv: 9800,
    amt: 2290,
  },
  {
    name: 'Page D',
    uv: 2780,
    pv: 3908,
    amt: 2000,
  },
  {
    name: 'Page E',
    uv: 1890,
    pv: 4800,
    amt: 2181,
  },
  {
    name: 'Page F',
    uv: 2390,
    pv: 3800,
    amt: 2500,
  },
  {
    name: 'Page G',
    uv: 3490,
    pv: 4300,
    amt: 2100,
  },
];

export default async function Dashboard() {
  const tiles: DashboardTile[] = [
    {id: '1', title: 'Crashes per day', data: data}, 
    {id: '2', title: 'Age for crashes', data: data}
  ];

  return (
    <Stack padding={5} spacing={1}>
      <Typography variant='h3'>Dashboard</Typography>
      <Grid container spacing={1}>
        {tiles.map((tile) => (
          <Grid item xs={3}>
            <Card sx={{padding: 5}}>
              <Typography variant='h6'>{tile.title}</Typography>            
              <ResponsiveContainer width={250} height={150}>
                <BarChart width={250} height={150} data={tile.data}>
                  <Bar dataKey="uv" fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
              <Button>See more</Button>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Stack>
  )
}
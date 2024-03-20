'use client'
import { getAllDashboardTiles } from '@/lib/queries';
import { Button, Card, Grid, Link, Stack, Typography } from '@mui/material'
import { Bar, BarChart, ResponsiveContainer } from 'recharts';
// import { testTiles } from '../test-data';

export default async function Dashboard() {

  const testTiles = await getAllDashboardTiles();

  return (
    <Stack spacing={1}>
      <Typography variant='h3'>Dashboard</Typography>
      <Grid container spacing={1}>
        {testTiles?.map((tile) => (
          <Grid item xs={3}>
            <Card sx={{padding: 5}}>
              <Typography variant='h6'>{tile.title}</Typography>            
              <ResponsiveContainer width={250} height={150}>
                <BarChart width={250} height={150} data={tile.data}>
                  <Bar dataKey={Object.keys(tile.data[0])[1]} fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
              <Link href={`/dashboard/${tile.id}`}>
                <Button>See more</Button>
              </Link>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Stack>
  )
}
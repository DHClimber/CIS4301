'use client'
import { BackButton } from '@/components/shared/back-button'
import { getDashboardTileById } from '@/lib/queries'
import { Box, Stack, Typography } from '@mui/material'
import { notFound } from 'next/navigation'
import { Bar, BarChart, CartesianGrid, Legend, Rectangle, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

/**
 * The individual tile view page.
 */
export default async function Page({params}: {params: {slug: string}}) {

  const dashboardTile = await getDashboardTileById(params.slug)

  if (!dashboardTile) {
    notFound()
  }

  return (
    <Box>
        <Stack direction='row' alignItems={'center'} gap={2} marginBottom={2}>
            <BackButton />
            <Typography variant='h4'>{dashboardTile.title}</Typography>
        </Stack>
        <ResponsiveContainer width={700} height={500}>
            <BarChart
                width={700}
                height={500}
                data={dashboardTile.data}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                }}
                >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="numCrashes" fill="#8884d8" activeBar={<Rectangle fill="pink" stroke="blue" />} />
            </BarChart>
        </ResponsiveContainer>
    </Box>
  )
}
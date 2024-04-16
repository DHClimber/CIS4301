'use client'
import { BackButton } from '@/components/shared/back-button'
import FilterControls from '@/components/shared/filter-controls'
import { generateHexColorFromLetter, getKeysForData } from '@/lib/functions'
import { getAllFilteredTiles, getDashboardTileById } from '@/lib/queries'
import { DashboardTile, FilterValues } from '@/lib/types'
import { Box, CircularProgress, Stack, Typography } from '@mui/material'
import { notFound } from 'next/navigation'
import { useEffect, useState } from 'react'
import { Bar, BarChart, CartesianGrid, Legend, Rectangle, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

/**
 * The individual tile view page.
 */
export default async function Page({params}: {params: {slug: string}}) {
  const [tile, setTile] = useState<DashboardTile>();
  const [keys, setKeys] = useState<string[]>();

  useEffect(() => {
    (async () => {
      const dashTile = await getDashboardTileById(params.slug);
      setTile(dashTile);
      if (dashTile) {
        setKeys(getKeysForData(dashTile.data));
      }
    })();
  }, []);

  const onFiltersSubmit = async (filters: FilterValues) => {
    // call backend with controls 
    const newData = await getAllFilteredTiles(filters);
    setTile(newData);
    if (newData) {
      setKeys(getKeysForData(newData.data));
    }
  }

  if (!tile) {
    notFound()
  }

  return (
    <Box>
      <Stack direction='row' alignItems={'center'} gap={2} marginBottom={2}>
          <BackButton />
          <Typography variant='h4'>{tile.title}</Typography>
      </Stack>
      <FilterControls ageRange weather datePicker sexSelect onSubmit={onFiltersSubmit} />
      <ResponsiveContainer width={700} height={500}>
        <BarChart
            width={700}
            height={500}
            data={tile.data}
            margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey={'name'} label={tile.xAxisLabel}/>
            <YAxis label={tile.yAxisLabel} />
            <Tooltip />
            <Legend />
            {keys ? keys.map((key: string) => {
              const color = generateHexColorFromLetter(key.charCodeAt(0));
              return <Bar dataKey={key} fill={`#${color}`} />
            }) : (
              <CircularProgress />
            )}
        </BarChart>
      </ResponsiveContainer>
    </Box>
  )
}
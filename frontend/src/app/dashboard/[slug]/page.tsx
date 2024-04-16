'use client'
import { BackButton } from '@/components/shared/back-button'
import FilterControls from '@/components/shared/filter-controls'
import { generateHexColorFromLetter, getKeysForData } from '@/lib/functions'
import { getAllFilteredTiles, getDashboardTileById, getFilteredDataForTileById } from '@/lib/queries'
import { DashboardTile, FilterValues } from '@/lib/types'
import { Box, CircularProgress, Stack, Typography } from '@mui/material'
import { notFound } from 'next/navigation'
import { useEffect, useState } from 'react'
import { Bar, BarChart, CartesianGrid, Label, Legend, Rectangle, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

/**
 * The individual tile view page.
 */
export default function Page({params}: {params: {slug: string}}) {
  const [tile, setTile] = useState<DashboardTile>();
  const [keys, setKeys] = useState<string[]>([]);

  useEffect(() => {
    console.log(params.slug);
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
    console.log("Filters " + filters);
    const newData = await getFilteredDataForTileById(filters, params.slug);
    console.log("New Data " + newData);
    setTile(newData);
    if (newData) {
      setKeys(getKeysForData(newData.data));
    }
  }

  return (
    <Box>
      <Stack direction='row' alignItems={'center'} gap={2} marginBottom={2}>
          <BackButton />
          <Typography variant='h4'>{tile?.title}</Typography>
      </Stack>
      <Stack direction='row' alignItems={'center'} gap={4}>
        <FilterControls ageRange weather datePicker sexSelect onSubmit={onFiltersSubmit} />
        {tile && keys.length > 0 ? (
          <ResponsiveContainer width={700} height={500}>
          <BarChart
              width={700}
              height={500}
              data={tile?.data}
              margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={'YEAR'}/>
              <YAxis>
                <Label angle={-90} value={tile.yAxisLabel} position='insideLeft' style={{textAnchor: 'middle'}} />
              </YAxis>
              <Tooltip />
              <Legend />
              {keys.map((key: string) => {
                const color = generateHexColorFromLetter(key.charCodeAt(0));
                return <Bar dataKey={key} fill={`#${color}`} />
              })}
          </BarChart>
        </ResponsiveContainer>
        ): tile && tile.data.length === 0 ? (
          <Typography sx={{fontSize : 36}} color="text.primary">No data based upon Filters</Typography>) : (
          <CircularProgress />
        )}
      </Stack>
      
    </Box>
  )
}
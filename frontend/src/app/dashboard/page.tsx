import { Button, Card, Typography } from '@mui/material'
import {Metadata} from 'next'
import Image from 'next/image'
import Link from 'next/link'
import {notFound} from 'next/navigation'

/**
 * Default metadata.
 */
export const metadata: Metadata = {
  title: 'Dashboard',
  description: "CrashDash main dashboard"
}

/**
 * The blog homepage.
 *
 * @see https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts
 */
export default async function Dashboard() {
  const tiles = [{id: '1', title: 'Crashes per day'}, {id: '2', title: 'Age for crashes'}];

  return (
    <div>
        {tiles.map((tile) => (
          <Card sx={{margin: 5, padding: 5}}>
            <Typography variant='h6'>{tile.title}</Typography>
            Here goes the graph
            <Button>See more</Button>
          </Card>
        ))}
    </div>
  )
}
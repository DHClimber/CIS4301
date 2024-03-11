import config from '@/lib/config'
import { Button, Stack } from '@mui/material'
import Link from 'next/link'
import { LogoComponent } from './logo-component'

/**
 * The shared header component.
 */
export default function NavBar() {
  return (
    <header className="text-center sm:text-left">
        <Stack direction='row' alignItems={'center'} gap={4}>
            <h1>
                <Link href="/">
                    <LogoComponent />
                </Link>
            </h1>
            <nav className="flex flex-row gap-4">
                {config.nav.map((item, index) => (
                <Link
                    className="text-base underline hover:no-underline"
                    key={index}
                    href={{pathname: item.path}}
                    prefetch={false}
                >
                    <Button>{item.name}</Button>
                </Link>
                ))}
            </nav>
        </Stack>
    </header>
  )
}
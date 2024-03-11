import config from '@/lib/config'
import { ExplosionAsset } from "../../../public/assets";
import { Stack, Typography } from '@mui/material';

export function LogoComponent() {
    return(
        <Stack direction='row' alignItems='center'>
            <Typography variant='h4' fontStyle={'italic'} fontWeight={'bold'}>
                {config.siteName}
            </Typography>
            <span style={{left: -25, top: 10, zIndex: -1, position: 'relative'}}>
                <ExplosionAsset/>
            </span>
        </Stack>
    )
}
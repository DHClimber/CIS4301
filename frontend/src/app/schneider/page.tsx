'use client'
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import { getTupleCount } from "@/lib/queries";
import { useState } from 'react';

export default function Schneider() {

    const [tupleCount, setTupleCount] = useState<number | null>(0);

    return (
      <div>
        <Accordion>
        <AccordionSummary onClick={async () => (setTupleCount(await getTupleCount()))}
          expandIcon={<ArrowDownwardIcon />}
          aria-controls="panel1-content"
          id="panel1-header"
        >
          <Typography sx={{fontSize: 36}} color="text.secondary">Tuple Count of 3 Tables</Typography>
        </AccordionSummary>
        <AccordionDetails>
            <Typography sx={{fontSize : 72}} color="text.primary" display="inline">
              The Tuple Count is 
            </Typography>
            <Typography sx={{fontSize : 72, color: "#0a65a7"}} display="inline"> {tupleCount?.toLocaleString()}</Typography>
        </AccordionDetails>
      </Accordion>
    </div>
    );
  }
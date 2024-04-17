'use client'
import Image from "next/image";
import styles from "./page.module.css";
import { ResponsiveContainer } from "recharts";
import { Typography } from "@mui/material";
import { TwitterTimelineEmbed } from "react-twitter-embed";

export default function Home() {

  return (
    <main className={styles.main}>
      <Typography sx={{mb : 2}}variant="h2">Accident Timeline</Typography>
      <ResponsiveContainer width={1000} height={1200}>
        <TwitterTimelineEmbed
          sourceType="profile"
          screenName="TotalTrafficCHI"
          options={{height: 800}}
        />
      </ResponsiveContainer>
    </main>
  );
}

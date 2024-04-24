'use client'
import styles from "./page.module.css";
import { ResponsiveContainer } from "recharts";
import { Typography } from "@mui/material";
import { TwitterTimelineEmbed } from "react-twitter-embed";

export default function Home() {

  return (
    <main className={styles.main}>
      {/* Bio Section */}
      <section className={styles.bio}>
        <Typography variant="h2" style={{ color: '#007bff', marginBottom: '20px', textAlign: 'center', fontSize: '36px' }}>Welcome to CrashDash!</Typography>
        <Typography variant="body1" style={{ fontSize: '24px', lineHeight: '1.6', color: '#000000', textAlign: 'center', maxWidth: '800px', margin: '0 auto' }}>
          CrashDash is your comprehensive platform for exploring traffic accident data in Chicago. We provide real-time and historical insights to help you navigate the city's roads safely.
        </Typography>
        <br />
        <Typography variant="h4" style={{ color: '#007bff', marginBottom: '10px', textAlign: 'center', fontSize: '36px' }}>What We Offer:</Typography>
        <ul style={{ listStyleType: 'disc', paddingLeft: '20px', marginBottom: '20px', textAlign: 'center' }}>
          <li><Typography variant="body1" style={{ color: '#000000', fontSize: '24px' }}>Real-Time and Historical Data: Access up-to-date and past information on traffic accidents throughout Chicago.</Typography></li>
          <li><Typography variant="body1" style={{ color: '#000000', fontSize: '24px' }}>Detailed Incident Overview: Explore the locations, severity, and contributing factors of accidents in the city.</Typography></li>
          <li><Typography variant="body1" style={{ color: '#000000', fontSize: '24px' }}>Interactive Visualizations: Navigate through the data effortlessly with intuitive features and engaging visuals.</Typography></li>
        </ul>
        <Typography variant="h4" style={{ color: '#007bff', marginBottom: '10px', textAlign: 'center', fontSize: '36px' }}>Our Mission:</Typography>
        <Typography variant="body1" style={{ fontSize: '24px', lineHeight: '1.6', color: '#000000', textAlign: 'center', maxWidth: '800px', margin: '0 auto' }}>
          At CrashDash, we're dedicated to promoting traffic safety and community awareness. Through data-driven insights, we aim to contribute to safer streets and efficient transportation systems in Chicago.
        </Typography>
        <br />
        <Typography variant="h4" style={{ color: '#007bff', marginBottom: '10px', textAlign: 'center', fontSize: '36px' }}>Join Us:</Typography>
        <Typography variant="body1" style={{ fontSize: '24px', lineHeight: '1.6', color: '#000000', textAlign: 'center', maxWidth: '800px', margin: '0 auto' }}>
          Join us in our mission to create safer streets and informed journeys in the Windy City. Together, let's make Chicago's roads safer for everyone.
        </Typography>
      </section>

      {/* Contributors Section */}
      <section className={styles.contributors} style={{marginTop: '30px', marginBottom: '50px' }}>
        <Typography variant="h3" style={{ color: '#007bff', marginBottom: '20px', textAlign: 'center', fontSize: '36px' }}>Contributors:</Typography>
        <ul style={{ listStyleType: 'none', padding: '0', margin: '0 auto', textAlign: 'center' }}>
          <li style={{ marginBottom: '10px', fontSize: '24px', color: '#000000' }}>Lucinda Quintal</li>
          <li style={{ marginBottom: '10px', fontSize: '24px', color: '#000000' }}>Daniel Hitchcock</li>
          <li style={{ marginBottom: '10px', fontSize: '24px', color: '#000000' }}>Connor Curcio</li>
          <li style={{ marginBottom: '10px', fontSize: '24px', color: '#000000' }}>Scott Willard</li>
          <li style={{ marginBottom: '10px', fontSize: '24px', color: '#000000' }}>Matthew Kerekes</li>
          {/* Add more contributors as needed */}
        </ul>
      </section>

      <Typography variant="h2" style={{ color: '#007bff', marginBottom: '20px', textAlign: 'center', fontSize: '36px' }}>Recent Accident Timeline</Typography>

      {/* Twitter Timeline */}
      <ResponsiveContainer width={1000} height={800} style={{ margin: '0 auto', marginBottom: '50px' }}>
        <TwitterTimelineEmbed
          sourceType="profile"
          screenName="TotalTrafficCHI"
          options={{ height: 800 }}
        />
      </ResponsiveContainer>
    </main>
  );
}

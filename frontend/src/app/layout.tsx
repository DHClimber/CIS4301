import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import NavBar from "@/components/shared/navbar";
import { Box } from "@mui/material";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "CrashDash",
  description: "CIS4301 project",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Box style={{margin: 15}}>
          <NavBar />
          <Box style={{padding: 50}}>
            {children}
          </Box>
        </Box>
      </body>
    </html>
  );
}

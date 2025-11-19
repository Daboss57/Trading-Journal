import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "Trading Journal",
  description: "Paper trading and backtesting workspace"
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "My Little Gatherer",
  description: "A local model question workspace.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
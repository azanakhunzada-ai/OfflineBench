import "./globals.css";

export const metadata = {
  title: "Offline AI Benchmark Lab",
  description: "Local AI assistant and model benchmark laboratory"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body>{children}</body></html>;
}

import { UserProvider } from "@auth0/nextjs-auth0/client";
import CssBaseline from "@mui/material/CssBaseline";
import Drawer from "./components/drawer";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <UserProvider>
        <body>
          <CssBaseline />
          <Drawer>{children}</Drawer>
        </body>
      </UserProvider>
    </html>
  );
}

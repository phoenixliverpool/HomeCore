import type { Metadata } from 'next'
import { Exo_2, Share_Tech_Mono } from 'next/font/google'
import './globals.css'

const exo2 = Exo_2({
  subsets: ['latin'],
  variable: '--font-exo2',
  weight: ['300', '400', '500', '600']
})

const shareTechMono = Share_Tech_Mono({
  subsets: ['latin'],
  variable: '--font-mono-tech',
  weight: '400'
})

export const metadata: Metadata = {
  title: 'HomeCore',
  description: 'Your home, under control.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${exo2.variable} ${shareTechMono.variable}`}>
        {children}
      </body>
    </html>
  )
}
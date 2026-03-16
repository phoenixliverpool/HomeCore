import DeviceGrid from 

export default function Home() {
  return (
    <div className="min-h-screen" style={{ background: '#0a0e14' }}>

      {/* Header */}
      <header style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '14px 24px',
        borderBottom: '0.5px solid #1e2a38',
        background: '#080c11'
      }}>
        <div style={{
          fontFamily: 'var(--font-mono-tech)',
          fontSize: '18px',
          color: '#38d9a9',
          letterSpacing: '3px'
        }}>
          HOME<span style={{ color: '#4dabf7' }}>CORE</span>
        </div>
        <div style={{
          fontFamily: 'var(--font-mono-tech)',
          fontSize: '11px',
          color: '#4a6275',
          letterSpacing: '1px',
          display: 'flex',
          alignItems: 'center',
          gap: '8px'
        }}>
          <span style={{
            width: '6px', height: '6px',
            borderRadius: '50%',
            background: '#38d9a9',
            display: 'inline-block'
          }} />
          SYSTEM ONLINE
        </div>
      </header>

      {/* Main content */}
      <main style={{ padding: '20px 24px' }}>
        <StatsBar />

        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr 1fr',
          gap: '16px',
          marginTop: '16px'
        }}>
          <div style={{ gridColumn: 'span 2' }}>
            <DeviceGrid />
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <WeatherCard />
            <NotesCard />
          </div>
        </div>
      </main>

    </div>
  )
}
import { NextResponse } from 'next/server'
import { prisma } from '@/lib/db'

// GET all devices
export async function GET() {
  try {
    const devices = await prisma.device.findMany({
      orderBy: { name: 'asc' }
    })
    return NextResponse.json(devices)
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch devices' },
      { status: 500 }
    )
  }
}

// POST a new device
export async function POST(request: Request) {
  try {
    const body = await request.json()
    const { name, ipAddress, type, room } = body

    const device = await prisma.device.create({
      data: { name, ipAddress, type, room }
    })
    return NextResponse.json(device, { status: 201 })
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create device' },
      { status: 500 }
    )
  }
}

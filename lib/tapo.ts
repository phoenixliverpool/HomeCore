import { loginDeviceByIp } from 'tp-link-tapo-connect'

const email = process.env.TAPO_EMAIL!
const password = process.env.TAPO_PASSWORD!

export async function getBulb(ipAddress: string) {
  const device = await loginDeviceByIp(email, password, ipAddress)
  return device
}

export async function turnBulbOn(ipAddress: string) {
  const device = await getBulb(ipAddress)
  await device.turnOn()
}

export async function turnBulbOff(ipAddress: string) {
  const device = await getBulb(ipAddress)
  await device.turnOff()
}

export async function setBrightness(ipAddress: string, brightness: number) {
  const device = await getBulb(ipAddress)
  await device.setBrightness(brightness)
}

export async function getBulbStatus(ipAddress: string) {
  const device = await getBulb(ipAddress)
  const info = await device.getDeviceInfo()
  return info
}

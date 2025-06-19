from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502) 
client.connect()

result = client.read_coils(address=0, count=1)
print("Read Coils:", result.bits)

client.close()

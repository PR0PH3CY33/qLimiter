
try:

	import psutil

	from time import sleep

	import os

except ImportError:

	print("Download psutil through pip3")




def getNetworkUsage(networkInterface):

	networkInputOutput = psutil.net_io_counters(pernic=True)

	networkUsage = networkInputOutput[networkInterface].bytes_sent + networkInputOutput[networkInterface].bytes_recv

	return networkUsage




def main():

	networkInterface = ""		#the network interface you want to monitor internet usage on

	networkLimit =  1000      #the maximum quota the interface should not exceed. the number is in bytes so dont forget conversion.

	while True:

		networkUsage = getNetworkUsage(networkInterface)

		if(networkUsage > networkLimit):

			#do an action when the network usage exceeds network limit

		else:

			sleep(1)

			pass



main()

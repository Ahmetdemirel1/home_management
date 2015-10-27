from django.shortcuts import render

port = "/dev/ttyACM0"

# Create your views here.

def index(request):
        from .models import Device,Sensor
        devices = Device.objects.all()
	sensors = Sensor.objects.all()
	for sensor in sensors:
		sensor.value = rcv_signal(sensor.signal)

        context = {'devices' : devices, 'sensors' : sensors}
        return render(request, 'on_off/index.html', context)

# Get devices list, and their state.
# Then send them all to template. The template will decide what to do with the data.

def signal(request, signal):
	from .models import Device
	#is it on signal?
	try:
		device = Device.objects.filter(signal_on=signal).get()
		device.on = True
		device.save()
		send_signal(signal)
	except:# off signal
		device = Device.objects.filter(signal_off=signal).get()
		device.on = False
		device.save()
		send_signal(signal)
	return index(request)

def reset(request):
	from .models import Device
	devices = Device.objects.all()
	for device in devices:
		device.on = False
		device.save()
	return index(request)

def send_signal(signal):
	import serial
	import time
	
	s = serial.Serial(port=port, baudrate=9600)
	# ardiuno initiates slowly
	time.sleep(1)
	s.write(signal)

def rcv_signal(signal):
	# send signal and recieve 4 digits - analog signal
	import serial
	import time

	s = serial.Serial(port=port, baudrate=9600)
	# ardiuno initiates slowly
	time.sleep(1)
	s.write(signal)

	# now read the signal and convert it
	rcv = s.read(4)
	rcv = float(rcv)
	temp = rcv*5.0/1024.0
	temp = temp - 0.5
	temp = temp / 0.01

	return int(temp)

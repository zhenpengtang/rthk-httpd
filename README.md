#RTHK Radio on2 Raspberry pi or Linux
You can Control the Radio by http://localhost:8888
Radio ON,Radio OFF,control the radio volume on web

###cookbook
tornado
supervisor
bootstrap


	rthk-httpd
	├── app.py			#main app
	├── conf
	│   ├── hkradio.conf		#supervisor conf
	│   └── hkradioweb.conf		#supervisor conf
	├── handle
	│   ├── __init__.py
	│   └── radio.py
	├── README.md
	└── www
	    └── index.html		#index.html


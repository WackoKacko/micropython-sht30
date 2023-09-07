# MicroPython driver for the amazing SHT30 temperature and humidity sensor 

So I made this because the original repo wouldn't run. There are/were some Python functions in there that didn't work in MicroPython. It now runs successfully (on an ESP32 WROOM).

I've used the first SHT30 module I found on eBay with good price and shipping time: [link](https://www.ebay.co.uk/itm/134684976674?chn=ps&mkevt=1&mkcid=28).

I've included a very simple example with non-blocking printing. For more methods and general info, visit the [original repo](https://github.com/rsc1975/micropython-sht30).

I've been developing in Pymakr on VSCode. It's pretty neat, I recommend it, despite its 2-star rating on the VSCode extensions page. Here's a nice tutorial on how to use it: [link](https://www.youtube.com/watch?v=YOeV14SESls). I've included a blinkLED example at the bottom of main.py in case you'd like a sanity check.

* [Sensor Datasheet](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf)  

_"Ahoy!"_ \
_-Popeye The Sailor_

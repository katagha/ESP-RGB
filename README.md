# ESP-RGB v1.0

ESP-RGB is a simple web-based RGB control project for ESP8266, where users can connect their devices to the ESP as an access point and control the RGB LED color via a color picker in the browser. 
![final](https://github.com/user-attachments/assets/058859eb-cf8f-4d8d-b005-ee9d063cbd14)

### Am working on the documentation 📄✨


## Features
- Control RGB LED using a color picker on the web page.
- Simple web server running on the ESP8266, handling both `GET` and `POST` requests.
- Allows setting the color of an RGB LED using a HEX code.
- Connect to the ESP-RGB device through a WiFi access point.
- files are separated for scalability

## Setup

### Requirements
- ESP8266 (or compatible device).
- MicroPython installed on the ESP8266.
- A web browser to control the RGB LED.

### Installing MicroPython on ESP8266 (and ESP-like devices)

#### Steps

1. **Download** the latest MicroPython binary for your microcontroller from [micropython.org](https://micropython.org/download).
2. **Install ESPTool** by downloading and installing [ESPTool](https://github.com/espressif/esptool).
3. **Connect your ESP8266**  
   - If your board has built-in USB (e.g., NodeMCU, Wemos D1 Mini), connect it directly via USB.  
   - Otherwise, use a USB-TTL adapter.  
4. **Find the serial port** for your device:  
   - **Linux/macOS:** Run `ls /dev/ttyUSB*` (commonly `/dev/ttyUSB0`).  
   - **Windows:** Check Device Manager (e.g., `COM3`).  
5. **Flash MicroPython** using the following command:  
   ```sh
   esptool.py --port <PORT> write_flash --flash_size=detect 0x0000 <PATH_TO_MICROPYTHON_BINARY>
### Files
- **main.py**: Python code running on the ESP8266, setting up the access point, handling web server requests, and controlling the RGB LED. 
> **_NOTE:_**  if you want the code to run when device is powered-on copy pace it to the `boot.py` file  
- **index.html**: The web page users interact with to control the LED color.
- **main.css**: Stylesheet to beautify the user interface.
- **Home.js**: JavaScript that sends the selected color to the server via a POST request.

### Instructions

1. copy the files to the ESP8266 flash memory 
   #### Copying Files to ESP8266 Flash Using Thonny

      The easiest way to copy files to the ESP8266 flash is by using Thonny's text editor.

   ##### Steps:

      1. Launch **Thonny**.
      2. Go to **Run > Configure Interpreter** and  Select **MicroPython (ESP8266)** as the interpreter.
      
      3. In the **Port** dropdown, select your **ESP8266 board**.
      
      4.  You should see in the shell somthing like :
      `MicroPython v1.24.1 on 2024-11-29; ESP module with ESP8266  
      Type "help()" for more information.`
      
      5. Open the file you want to upload (e.g., `index.html`) by going to **File > Open**.
      6. Go to **File > Save Copy As** and Choose **MicroPython device** 
      7. Enter the correct file name (e.g., `index.html`), and save it directly to the ESP8266 flash storage.
> **_NOTE:_**  if you want the code to run when device is powered-on copy pace it to the `boot.py` file  
2. Run the `main.py` 
3. The ESP8266 will start as an access point (SSID: `ESP-RGB`, password: `test1234`).
4. Connect your device to the ESP-RGB WiFi network.
5. Open the web page served by the ESP8266 in your browser (you can use the IP `http://10.0.0.1:8080/index.html`).
6. Use the color picker to select the desired color and click "Send" to update the RGB LED.

## License
This project is open-source and free to use. Feel free to contribute!



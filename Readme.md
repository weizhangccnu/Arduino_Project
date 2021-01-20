## Arduino Project
### 1. Install Arduino IDE (Integrated development environment)
  - You can download the Arduino IDE form the website: [Arduino IDE](https://www.arduino.cc/en/software/)
### 2. Arduino Language Reference
  - This website page listed all the language reference for Arduino: [Language Reference](https://www.arduino.cc/reference/en/)
### 3. A simple example to illustrate how to use Arduino IDE.
  - Turns an LED on for a few seconds, then off for a few seconds, repeatedly.
```
int led = 13;				// define led port, see the schematic

void setup(){				// initial pin mode
	pinMode(led, OUTPUT);		// define pin mode
}

void loop(){				// equal to main function 
	digitalWrite(led, HIGH);	// turn on led
	delay(200);			// delay 200 ms
	digitalWrite(led, LOW);		// turn off led
	delay(200);			// delay 200 ms
}	

```

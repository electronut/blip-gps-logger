# GPS Logger

Last weekend, my colleagues and I decided to go on a trek to Kudremukh peak in the Western Ghats. We thought, how about recording the GPS data throughout the trek. We quickly assembled a GPS module with our upcoming board blip, which is a development board based on Nordic's [nRF52840](https://openthread.io/platforms/nrf52840) chip. Blip has onboard SD card slot which made our job easier, to collect and store data.

![](bli_gps_connection.jpg)

## Hardware used
* [blip](https://docs.electronut.in/ElectronutLabs-blip/)
* [U-Blox GPS module](https://robu.in/product/ublox-neo-6m-gps-module/)
* A box

![](blip_gps.jpg)

![](blip_in_box.jpg)

Later, we planned to upload GPS data to the [Google Earth](https://www.google.com/intl/en_in/earth/) to plot the trail. We used a normal power bank to power the blip and GPS module. We kept it in the outside pocket of the backpack.

![](backpack.jpg)

The trek started. We covered more than 20 km both ways, the view was breathtaking. It was definitely an exhilarating experience. 

![](medow2.jpg)

After returning we were excited to upload the collected GPS data to google earth. After connecting the SD card and scanning the data for while, we realized that we have missed several hours of data, this what happens when you code in haste :P. But that's okay at least we were able to plot some data points. We converted the GPS data in KML format and plotted to Google Earth. We were happy to see our somewhat successful attempt and that was enough for us.

![](google_earth_path.jpg)

Top view

![](google_e_top.jpg)

If you wish to see the firmware and scripts for the code, you can find the link below. At last, I want to thank all my colleagues at Electronut Labs especially  Ajay for helping me complete the project. 

## Firmware and scripts 

Happy Trecking and Happy Coding! :)
![](trek_shoes.jpg)

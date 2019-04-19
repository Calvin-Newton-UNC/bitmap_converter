
#                           #
#   Bitmap Converter Tool   #
#                           #



- Converts 16 pixel wide bitmap files (file extension .bmp) to the format 
required for bmem.mem

- Create a bitmap file in microsoft paint and draw 16x16 squares in a column. 
The top square will be charcode 0, next square below is charcode 1, etc.

- Place bitmap_convert.exe and your bitmap file in your project folder that 
you want to generate bmem.mem in

- Run bitmap_convert.exe when you want to update bmem.mem with your bitmap file

- The first time running it will prompt for the name of the bitmap file

- A bitmap_convert.config file will then be generated so you don't need to enter
the file name in again. Just be sure to delete the config file and rerun if you 
change you bitmap file name.

- See example bitmap

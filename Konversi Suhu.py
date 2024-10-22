def konversisuhu(temperature, value): # Membuat fungsi untuk konversi suhu
    if value == 'C' : # Membuat kondisi if
        temperaturesuhu = (temperature - 32) * 5/9  # Rumus untuk konversi Fahrenheit ke Celsius
        return temperaturesuhu, 'C'  # Kembalikan hasil konversi beserta satuan Celsius
    else: # Membuat kondisi else jika value bukan C
        temperaturesuhu = (temperature * 9/5) + 32  # Rumus untuk konversi Celsius ke Fahrenheit
        return temperaturesuhu, 'F'  # Kembalikan hasil konversi beserta satuan Fahrenheit

# Konversi dari Celsius ke fahrenheit
celsius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

# Konversi dari Fahrenheit ke Celsius
fahrenheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")

import pycdlib

# Create an ISO file
iso = pycdlib.PyCdlib()
iso.new(interchange_level=3, joliet=True)

# Add a file to the ISO
iso.add_file("shatter", "/shatter")

# Write the ISO file
iso.write("OUTPUT.iso")
iso.close()
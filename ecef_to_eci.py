# ecef_to_eci.py
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Pramil Patel
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137
# helper functions
w = 7.2921150e-5

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
# if len(sys.argv)==3:
#   arg1 = sys.argv[1]
#   arg2 = sys.argv[2]
#   ...
# else:
#   print(\
#    'Usage: '\
#    'python3 arg1 arg2 ...'\
#   )
#   exit()

# write script below this line

def ymdhms_to_jd(year, month, day, hour, minute, second):
    if month <= 2:
        year -= 1
        month += 12
    jd = math.floor(365.25*(year+4716)) + math.floor(30.6001*(month+1)) + day + (2-(math.floor(year/100)) + math.floor((math.floor(year/100))/4)) - 1524.5
    day_fract = (hour + (minute/60) + (second/3600)) / 24
    return jd + day_fract

# def jd_to_gst(jd):
#     T_UT1 = (jd - 2451545)/36525
#     secGMST = 67310.54841 + (((876600*60*60)+8640184.812866)*T_UT1) + (0.093104*(T_UT1**2)) - (6.2e-6*(T_UT1**3))
#     GST_rad = math.fmod(secGMST%86400*w+2*math.pi, 2*math.pi)
#     return GST_rad

def ecef_to_eci(jd, ecef_x_km, ecef_y_km, ecef_z_km):
    T_UT1 = (jd - 2451545)/36525
    secGMST = 67310.54841 + (((876600*60*60)+8640184.812866)*T_UT1) + (0.093104*(T_UT1**2)) - (6.2e-6*(T_UT1**3))
    GST_rad = math.fmod(secGMST%86400*w+2*math.pi, 2*math.pi)

    eci_x_km = ecef_x_km*math.cos(-GST_rad)+ecef_y_km*math.sin(-GST_rad)
    eci_y_km = ecef_y_km*math.cos(-GST_rad)-ecef_x_km*math.sin(-GST_rad)
    eci_z_km = ecef_z_km
    
    return eci_x_km, eci_y_km, eci_z_km

if len(sys.argv) == 10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    ecef_x_km = float(sys.argv[7])
    ecef_y_km = float(sys.argv[8])
    ecef_z_km = float(sys.argv[9])
else:
    print('Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km')
    exit()

jd = ymdhms_to_jd(year, month, day, hour, minute, second)

eci_x_km, eci_y_km, eci_z_km = ecef_to_eci(jd, ecef_x_km, ecef_y_km, ecef_z_km)

print(eci_x_km)
print(eci_y_km)
print(eci_z_km)
# import geocoder
# from geopy.geocoders import Nominatim

# g = geocoder.ip('me')
# coordinate = g.latlng

# def loc_addr(latitude, longitude):

	# upnm_lat = 3.0505
	# upnm_long = 101.7248
	
	# diff_lat = upnm_lat - latitude
	# diff_long = upnm_long - longitude
	
	# curr_lat = latitude + diff_lat
	# curr_long = longitude + diff_long
	# curr_lat = str(curr_lat)
	# curr_long = str(curr_long)
	
	# final_crd = "%s,%s" % (curr_lat,curr_long)
	# geoLoc = Nominatim(user_agent="GetLoc")
	# locname = geoLoc.reverse(final_crd)
	# print(locname.address)

# loc_addr(coordinate[0],coordinate[1])

from xpxchain import models

account = models.Account.generate_new_account(models.NetworkType.MIJIN_TEST)

print(account.public_key)
print(account.private_key)




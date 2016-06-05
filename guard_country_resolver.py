import sys

if sys.version_info[0] == 2:
    input = raw_input

# Five eye countries and Israel
FIVE_EYES_I = ['us','ca','gb','nz','au','il']

# This excludes US because a lot of exit trafic goes to the us anyways and this should also help reduce distinguishability. 
FOUR_EYES_I = ['ca','gb','nz','au','il']

# America and their guards
AMERICA_S = ['ar','bo','br','cl','co','ec','gf','gy','py','pe','sr','uy','ve']
AMERICA_C = ['mx','cu','ht','dm','jm','pa','gt','hn','ni','cr','bs','bz']
AMERICA_TARGETS = AMERICA_S + ['pt','es','za'] 

# Maghreb countries and close european countries as guards
MAGHREB = ['ml', 'mr', 'eh', 'ma', 'dz', 'tn', 'ly']
MAGHREB_TARGETS = ['pt','es','fr','it','gr']

# South east asia.
SEA = ['jp', 'kr', 'tw', 'hk', 'sg', 'vn']

# European peninsula countries
EUROPEAN_TARGETS = MAGHREB_TARGETS + ['de','nl','ch','se', 'dk','be','lu','at','cz','pl','ro','lv', 'ee','lt','no','ua','ru','si','sk','hr','rs','bg', 'hu', 'fi','md','pl']

# Basically all countries with relays, omitting FIVE_EYES_I
OTHERS_TARGETS = EUROPEAN_TARGETS + AMERICA_S + SEA

# Profiles for larger Tor countries:
guard_resolver = dict([
	( 'de' , ['de', 'nl', 'lu', 'ch', 'pl', 'dk'] ),
	( 'ch' , ['ch', 'de', 'fr','it','at'] ),
	( 'at' , ['at','it','ch','de','cz','hu','si','sk'] ),
	( 'cz' , ['cz','de','pl','at','sk'] ),
	( 'pl' , ['pl', 'de', 'cz','si','ua'] ),
	( 'dk' , ['dk','de','se','no','is'] ),
	( 'se' , ['se', 'no', 'dk','fi','is'] ),
	( 'nl' , ['nl', 'be','de','lu','fr'] ),
	( 'be' , ['be', 'fr', 'nl', 'lu','de'] ),
	( 'lu' , ['lu','nl','be','fr','de'] ),
	( 'fr' , ['fr', 'es','ch','be'] ),
	( 'gb' , ['gb', 'ie', 'fr','be','nl'] ),
	( 'uk' , ['gb', 'ie', 'fr','be','nl'] ),
	( 'us' , ['us', 'ca'] ),
	( 'ca' , ['ca', 'us'] ),
	( 'il' , ['il', 'tr', 'gr', 'it', 'ro','ua','ru'] ),
	( 'au' , ['au', 'nz'] + SEA ),
	( 'nz' , ['au', 'nz'] + SEA ),
	( 'ro' , ['ro','md','ua','tr','hu'] ),
	( 'ru' , ['ru', 'no', 'lv', 'ee', 'lt', 'ua'] ),
	( 'lv' , ['ru', 'lv', 'ee', 'lt'] ),	
	( 'ee' , ['ru', 'lv', 'ee', 'lt'] ),	
	( 'lt' , ['ru', 'lv', 'ee', 'lt'] ),
	( 'it' , ['it','fr','gr','ch','at','hr','si'] ),
	( 'ua' , ['ua', 'ro', 'md','pl','ru'] ),
	( 'md' , ['ua', 'ro', 'md'] ),
	( 'gr' , ['gr', 'it', 'tr', 'hr', 'ro'] ),
	( 'pt' , ['pt', 'es', 'fr'] ),
	( 'es' , ['pt', 'es', 'fr'] ),
	( 'tr' , ['tr', 'gr', 'it', 'ro','ua','ru'] ),
	( 'hu' , ['hu', 'at', 'cz', 'pt', 'ro'] ),
	( 'is' , ['is', 'dk','no','se'] ),
	( 'no' , ['no', 'dk','se','is'] ),
	( 'africa' , EUROPEAN_TARGETS + ['za'] ),
	( 'southeastasia' , SEA + ['ru']),
	( 'america' , AMERICA_TARGETS ),
	( 'europe' , EUROPEAN_TARGETS ),
	( 'other' , OTHERS_TARGETS )
	])

#
# Regions that guard each other:
#
for country in SEA:
	guard_resolver[country] = SEA + ['ru']

for country in AMERICA_S:
	guard_resolver[country] = AMERICA_TARGETS
	
for country in AMERICA_C:
	guard_resolver[country] = AMERICA_TARGETS + [country]

for country in MAGHREB:
	guard_resolver[country] = MAGHREB_TARGETS + [country]

def guards_close_to_home(resolver=guard_resolver):
	country_code = input("\nWhat is your two letter country code?\n").lower()
	if country_code in resolver:
		return resolver[country_code], country_code
	else:
		print( "\nCountry code '" + country_code + "' not known." )
		print( "Try other code or one of the general regions:" )
		print( "africa, southeastasia, america, europe, other" )
		return guards_close_to_home(resolver)
	
if __name__=="__main__":
	# This is used only during development
	print( guards_close_to_home() )
	

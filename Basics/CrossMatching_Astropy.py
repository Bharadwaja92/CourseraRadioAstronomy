from astropy.coordinates import SkyCoord
from astropy import units as u

coords1 = [[270, -30], [185, 15]]
coords2 = [[185, 20], [280, -30]]

sky_cat1 = SkyCoord(coords1*u.degree, frame='icrs')
sky_cat2 = SkyCoord(coords2*u.degree, frame='icrs')

closest_ids, closest_dists, closest_dists3d = sky_cat1.match_to_catalog_sky(sky_cat2)

print(closest_ids)
print(closest_dists)
print(closest_dists3d)

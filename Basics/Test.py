import astropy.units as u
import astropy.coordinates as coord

icrs = coord.ICRS(ra=258.58356362*u.deg, dec=14.55255619*u.deg,
                  radial_velocity=-16.1*u.km/u.s)

v_sun = coord.Galactocentric.galcen_v_sun.to_cartesian()

gal = icrs.transform_to(coord.Galactic)
cart_data = gal.data.to_cartesian()
unit_vector = cart_data / cart_data.norm()

v_proj = v_sun.dot(unit_vector)

rv_gsr = icrs.radial_velocity + v_proj
print(rv_gsr)

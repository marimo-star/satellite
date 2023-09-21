import skyfield.api
sats = skyfield.api.load.tle_file("https://celestrak.org/NORAD/elements/gnss.txt", reload=True)
len(sats)
sat = sats[0]
ts = skyfield.api.load.timescale()
sat.at(ts.now())
sat.at(ts.now()).position.m
sat.velocity.m_per_s

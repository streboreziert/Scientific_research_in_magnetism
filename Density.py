#Calculate denisty of ball
π= 3.14
Vresin= 1.1 # resin volume
Qresin= 1 # resin density
d= 3 # sides of cube
Qcube= 3 # density of cube
rsphere = 3 # sphere radiuss
Qliqud = 2  # liquid density

Qliqud = 3*(Vresin*Qresin+d*d*d*Qcube)/(4*pi*rsphere*rsphere*rsphere)
Qresin = ((Qliqud * (4*pi*rsphere*rsphere*rsphere))- (3*d*d*d*Qcube))/(3*Vresin)

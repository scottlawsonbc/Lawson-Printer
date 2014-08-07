
class Item:
	def __init__(self, d, q, price, p, url):
		self.desc  		= d
		self.qty   		= q
		self.price 		= price
		self.printable 	= p
		self.url   		= url

def add(desc, qty, price, printable, url): bom.append(Item(desc,qty,price, printable,url))

bom = []

# MISUMI EXTRUSION
add('Black 2020 180mm',				1,		2.90, 		False,		r'http://us.misumi-ec.com/vona2/detail/110302368740/')
add('Black 2020 380mm',				3, 		3.34, 		False,		r'http://us.misumi-ec.com/vona2/detail/110302368740/')
add('Black 2020 400mm',				1,	 	3.52, 		False, 		r'http://us.misumi-ec.com/vona2/detail/110302368740/')
add('Black 2040 380mm',				1, 		6.34, 		False, 		r'http://us.misumi-ec.com/vona2/detail/110302368830/')
add('Black 2040 460mm',				2,		7.68,		False,		r'http://us.misumi-ec.com/vona2/detail/110302368830/')
# MISUMI PARTS
add('Heavy duty bracket', 			2, 		3.5, 		True,		r'http://us.misumi-ec.com/vona2/detail/110300437960/')
add('Reinforcement bracket+screws',	2, 		3.7,		True,		r'http://us.misumi-ec.com/vona2/detail/110302246060/?ProductCode=HPTBG5')		
add('Y-motor spacer', 				4, 		1.0, 		True,		r'http://us.misumi-ec.com/vona2/detail/110300234350/')
# MISUMI LEAD SCREW
add('1.5mm pitch lead screw 300mm', 2, 		38.54,		False,		r'http://us.misumi-ec.com/vona2/detail/110300083060/')
add('1.5mm pitch lead screw nut',	2, 		17.0,		False,		r'http://us.misumi-ec.com/vona2/detail/110300084910/')
# MISUMI LINEAR GUIDE
add('430mm steel slide',			1, 		49.96,		False, 		r'http://us.misumi-ec.com/vona2/detail/110300071860/')
	
# OPENBUILDS EXTRUSION
add('Black v-slot 2040 1000mm',		1,		15.83,		False,		r'http://openbuildspartstore.com/black-v-slot-20-x-40mm/')
add('Black v-slot 2020 1000mm',		1,		10.92,		False,		r'http://openbuildspartstore.com/v-slot-20-x-20mm/')
# OPENBUILDS WHEELS
add('Smooth idler pulley kit',		3, 		5.25,		False,		r'http://openbuildspartstore.com/smooth-idler-pulley-kit/')
add('Solid V Wheel kit',			12,		4.31,		False,		r'http://openbuildspartstore.com/openbuilds-solid-v-wheel-kit/')
# OPENBUILDS PLATES
add('2-hole joining plate',			4,		2.13,		True,		r'http://openbuildspartstore.com/2-hole-joining-strip-plate/')
add('Build plate',					1,		20.69,		False,		r'http://openbuildspartstore.com/build-plate/')
add('Motor mount plate',			1,		7.59,		False,		r'http://openbuildspartstore.com/motor-mount-plate/')
add('Threaded rod plate',			2,		7.59,		False,		r'http://openbuildspartstore.com/threaded-rod-plate/')
add('20mm gantry plate',			1,		6.55,		True,		r'http://openbuildspartstore.com/openrail-gantry-plate/')
# OPENBUILDS CONNECTORS/COUPLERS
add('90deg vslot corner connector', 4,		3.00,		True,		r'http://openbuildspartstore.com/90-degree-angle-corner-connector-v-slot/')
add('3-way cube corner connector',	4,		3.54,		True,		r'http://openbuildspartstore.com/three-way-cube-corner-connector-v-slot/')
add('Flexible coupling',			2, 		6.48, 		True,		r'http://openbuildspartstore.com/1-4-x-5mm-flexible-coupling/')
# OPENBUILDS BELTS/PULLEYS
add('Belt crimp clamp',				2, 		0.65,		True,		r'http://openbuildspartstore.com/belt-crimp-clamp/')
add('GT2 timing pulley',			2,  	5.45, 		False,		r'http://openbuildspartstore.com/gt2-2mm-aluminum-timing-pulley-20/')
add('GT2 belt (1-foot)', 			8,		2.72,		False,		r'http://openbuildspartstore.com/gt2-2mm-timing-belt/')

subtotal = 0.0
for b in bom: subtotal += b.price * b.qty
print 'Printable parts:\t\t', sum(x.printable for x in bom)
print 'Non-printable parts:\t', sum(not x.printable for x in bom)
print 'Total parts:\t\t\t', len(bom), '\r\n'

print 'Metal parts cost:', 	 '$' + str(sum(x.price*x.qty for x in bom))
print 'With printed parts:', '$' + str(sum(x.price*x.qty*(not x.printable) for x in bom))




# ALTERNATE PARTS

# Y-AXIS
	# BALL BEARING LINEAR GUIDE
		# SUB: add('400mm linear guide', 			1,		155.38,		r'http://us.misumi-ec.com/vona2/detail/110300044470/?HissuCode=SEL2BM20-220%2C280%2C340%2C400%2C460%2C520%2C580%2C640%2C700&PNSearch=SEL2BM20-400&CategorySpec=00000029026%3A%3A400')
		# SUB: add('460mm linear guide', 	1,	130.49,		r'http://us.misumi-ec.com/vona2/detail/110300044470/?Inch=0')
	# SIMPLIFIED ALUMINIUM GUIDE
		# SUB: add('430mm slide, 2 blocks', 1, 	69,			r'http://us.misumi-ec.com/vona2/detail/110300071610/?Inch=0#optionContainer')
	# STEEL LINEAR SLIDE
		# SUB: add('430mm Fe slide, 2 blk',	1, 	76.96,		r'http://us.misumi-ec.com/vona2/detail/110300071860/?Inch=0')
	# SUB: OpenBuilds Vslot rail

# LEAD SCREW
	#SUB: add('310mm lead screw with nut', 	2, 		18.95,		r'http://store.makerstoolworks.com/motion/z-axis-lead-screw-and-nut-single/'	

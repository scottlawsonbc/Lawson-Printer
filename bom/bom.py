
class Item:
	def __init__(self, d, q, price, p, url, misumiPartNum='', identifier=''):
		self.desc  			= d
		self.qty   			= q
		self.price 			= price
		self.printable 		= p
		self.url   			= url
		self.misumiPartNum 	= misumiPartNum
		self.identifier 	= identifier

bom = []
def add(desc, qty, price, printable, url, misumiPartNum='', identifier=''): bom.append(Item(desc,qty,price,printable,url,misumiPartNum,identifier))

# MISUMI EXTRUSION
add('Black 2020 400mm',				2,		3.52, 		False,		r'http://us.misumi-ec.com/vona2/detail/110302368740/', 'HFSB5-2020-400')
add('Black 2020 380mm',				2, 		3.34, 		False,		r'http://us.misumi-ec.com/vona2/detail/110302368740/', 'HFSB5-2020-380')
add('Black 2020 180mm',				1,	 	2.90, 		False, 		r'http://us.misumi-ec.com/vona2/detail/110302368740/', 'HFSB5-2020-180')
add('Black 2020 60mm',				1, 		2.90, 		False, 		r'http://us.misumi-ec.com/vona2/detail/110302368830/', 'HFSB5-2020-60')
add('Black 2020 50mm',				1,		2.90,		False,		r'http://us.misumi-ec.com/vona2/detail/110302368830/', 'HFSB5-2020-50')
add('Black HFSBz5-2040-460',		2,		7.68, 		False,		r'http://us.misumi-ec.com/vona2/detail/110302368740/', 'HFSB5-2040-460')
add('Black 2040 380mm',				1, 		6.34, 		False,		r'http://us.misumi-ec.com/vona2/detail/110302368740/', 'HFSB5-2040-380') 
# MISUMI PARTS, 
add('Heavy duty bracket', 			2, 		3.5, 		True,		r'http://us.misumi-ec.com/vona2/detail/110300437960/', 'HBLTDW5')
add('GT2 Pulley',					1,		16.11,		True,		r'http://us.misumi-ec.com/vona2/detail/110302193470/', 'GPA22GT2060-B-H4')
add('Shaft collar',					1,		11.00,		True,		r'http://us.misumi-ec.com/vona2/detail/110300022860/', 'SDSJ16-8')
# MISUMI BRACKETS, 
add('2-hole Thin bracket',			4,		1.02,		True,		r'http://us.misumi-ec.com/vona2/detail/110300438930/', 'HBLSS5')
add('4-hole bracket',				2,		1.6,		True,		r'http://us.misumi-ec.com/vona2/detail/110302245630/', 'HPTSSL5')
add('8-hole L bracket',				2,		4.25,		True,		r'http://us.misumi-ec.com/vona2/detail/110302245720/', 'HPTLD5')
add('4-hole L bracket',				4,		3.00,		True,		r'http://us.misumi-ec.com/vona2/detail/110302245720/', 'HPTLS5')
add('4-hole T bracket',				2,		2.75,		True,		r'http://us.misumi-ec.com/vona2/detail/110302245970/', 'HPTTS5')
# MISUMI LEAD SCREW, 
add('Precision lead screw', 		2,		30.93,		False,		r'http://us.misumi-ec.com/vona2/detail/110300082630/', 'MTSRA10-345-S12-Q6')
add('Lead screw nut',				2,		18.49,		False,		r'http://us.misumi-ec.com/vona2/detail/110300084910/', 'MTSNR10')
# MISUMI LINEAR GUIDE, 
#add('430mm steel slide',			1, 		50.99,		False, 		r'http://us.misumi-ec.com/vona2/detail/110300071860/', 'BJKSW20-430')
add('460mm awesome slide',			1,		150.0,		False,		r'http://us.misumi-ec.com/vona2/detail/110300044470/', 'SEL2BM20-460')

# OPENBUILDS EXTRUSION
add('Black V-Slot 20x40mm 1000mm',	1,		15.83,		False,		r'http://openbuildspartstore.com/black-v-slot-20-x-40mm/', 						identifier='OpenBuilds')
# OPENBUILDS FASTENERS	
add('OpenRail Black 1000mm',		1,		5.45,		False,		r'http://openbuildspartstore.com/openrail-black-anodized/', 					identifier='OpenBuilds')
add('25-pack T-nuts',				5,		5.40,		False,		r'http://openbuildspartstore.com/tee-nuts-25-pack/', 							identifier='OpenBuilds')
add('Low profile M5 6mm 25pack', 	3,		4.47,		False,		r'http://openbuildspartstore.com/low-profile-screws-m5/', 						identifier='OpenBuilds')
add('Low profile M6 8mm	25pack', 	2,		5.03, 		False,		r'http://openbuildspartstore.com/low-profile-screws-m5/', 						identifier='OpenBuilds')	
# OPENBUILDS WHEELS	
add('Smooth idler pulley kit',		3, 		5.25,		False,		r'http://openbuildspartstore.com/smooth-idler-pulley-kit/', 					identifier='OpenBuilds')
add('Solid V Wheel kit',			4,		4.31,		False,		r'http://openbuildspartstore.com/openbuilds-solid-v-wheel-kit/',		 		identifier='OpenBuilds')
#add('Solid V Wheel kit',			8,		4.31,		False,		r'http://openbuildspartstore.com/openbuilds-solid-v-wheel-kit/',		 		identifier='OpenBuilds')
add('Dual V Wheel metal kit',		4,		7.40,		False,		r'http://openbuildspartstore.com/openbuilds-dual-v-wheel-kit-metal/', 			identifier='OpenBuilds')
# OPENBUILDS PLATES	
add('2-hole joining plate',			6,		2.13,		True,		r'http://openbuildspartstore.com/2-hole-joining-strip-plate/', 					identifier='OpenBuilds')
add('Build plate',					1,		20.69,		False,		r'http://openbuildspartstore.com/build-plate/', 								identifier='OpenBuilds')
add('Motor mount plate',			1,		7.59,		False,		r'http://openbuildspartstore.com/motor-mount-plate/', 							identifier='OpenBuilds')
add('Threaded rod plate',			2,		7.59,		False,		r'http://openbuildspartstore.com/threaded-rod-plate/', 							identifier='OpenBuilds')
add('20mm gantry plate',			1,		6.55,		True,		r'http://openbuildspartstore.com/openrail-gantry-plate/', 						identifier='OpenBuilds')
# OPENBUILDS CONNECTORS/COUPLERS/SPACERS	
add('90deg vslot corner connector', 8,		3.00,		True,		r'http://openbuildspartstore.com/90-degree-angle-corner-connector-v-slot/', 	identifier='OpenBuilds')
add('5mm x 6mm coupler',			2,		5.83,		True,		r'http://openbuildspartstore.com/5mm-x-6mm-flexible-coupling/', 				identifier='OpenBuilds')
# OPENBUILDS SPACERS AND SHIMS	
add('Precision 1mm shim',			16,		0.27,		False,		r'http://openbuildspartstore.com/precision-shim-10x5x1mm/', 					identifier='OpenBuilds')
add('20mm aluminium spacer',		6,		0.49,		False,		r'http://openbuildspartstore.com/aluminum-spacers/', 							identifier='OpenBuilds')
add('0.25in nylon spacer',			12,		0.22,		False,		r'http://openbuildspartstore.com/nylon-spacer/', 								identifier='OpenBuilds')
add('Eccentric spacers',			6,		2.19,		False,		r'http://openbuildspartstore.com/eccentric-spacers/', 							identifier='OpenBuilds')
# OPENBUILDS BELTS/PULLEYS	
add('Belt crimp clamp',				4, 		0.65,		True,		r'http://openbuildspartstore.com/belt-crimp-clamp/', 							identifier='OpenBuilds')
add('GT2 timing pulley',			1,  	5.45, 		False,		r'http://openbuildspartstore.com/gt2-2mm-aluminum-timing-pulley-20/', 			identifier='OpenBuilds')
add('GT2 (2mm) belt (per-foot)', 	8,		2.72,		False,		r'http://openbuildspartstore.com/gt2-2mm-timing-belt/', 						identifier='OpenBuilds')
# OPENBUILDS MOTORS	
#add('NEMA 17 motor', 				4,		19.20,		False,		r'http://openbuildspartstore.com/nema-17-stepper-motor/', 						identifier='OpenBuilds')
add('NEMA 23 motor',				1,		26.88,		False,		r'http://openbuildspartstore.com/nema-23-stepper-motor/', 						identifier='OpenBuilds')
# OPENBUILDS ENDSTOPS
add('Endstop + mounting plate kit',	3,		4.92,		False,		r'http://openbuildspartstore.com/micro-limit-switch-kit-with-mounting-plate/', 	identifier='OpenBuilds')

# REPRAP DISCOUNT ELECTRONICS
#add('RUMBA electronics kit',		1, 		119.00,		False,		r'http://www.reprapdiscount.com/electronics/54-rumba-board-incl-6-a4988-driver.html', 	identifier='RepRap Discount')
add('MK2A Aluminium heat bed',		1,		29,			False,		r'http://www.reprapdiscount.com/electronics/73-aluminium-mk2a-heated-bed.html', 		identifier='RepRap Discount')

# E3D
add('E3D 1.75mm bowden',			1,		78.50,		False,		r'http://www.e3d-online.com', identifier='E3D')

subtotal = 0.0

for b in bom: subtotal += b.price * b.qty
print ('printable parts:\t\t', sum(x.printable*x.qty for x in bom))
print ('Non-printable parts:\t', sum((not x.printable)*x.qty for x in bom))
print ('Total parts:\t\t\t', sum(x.qty for x in bom), '\r\n')
print ('Metal parts cost:\t\t', 	 '$' + str(sum(x.price*x.qty for x in bom)))
print ('With printed parts:\t\t', '$' + str(sum(x.price*x.qty*(not x.printable) for x in bom)))

# For list of printable components
def printPrintable():
	printable = [x for x in bom if x.printable]
	for part in printable:
		print ("'''Qty:'''", part.qty, "'''Part:'''", part.desc)

# For Misumi BOM generation
def generateMisumiBOM():
	lines = []
	parts = [x for x in bom if len(x.misumiPartNum)>0]
	for i in range(len(parts)):
		ref = 'Part-' + str(i)
		prodCode = parts[i].misumiPartNum
		express = ''
		qty = parts[i].qty
		lines.append('\t%s,%s,%s,%i' % (ref, prodCode, express, qty))
	for line in lines:
		print (line)

# For RepRap wiki table
def generateMisumiWikiTable():
	lines = []
	parts = [x for x in bom if len(x.misumiPartNum)>0]
	# Header
	lines.append('====Misumi====')
	lines.append('{| class="wikitable"')
	lines.append('! Description')
	lines.append('! Part Number')
	lines.append('! Quantity')
	lines.append('! Unit Cost (USD)')
	lines.append('! Total (USD)')
	# Add entry for each part
	for i in range(len(parts)):
		lines.append('|-')
		lines.append('|%s' % parts[i].desc)
		lines.append('|[http://us.misumi-ec.com/vona2/result/?Keyword=%s %s]' % (parts[i].misumiPartNum, parts[i].misumiPartNum))
		lines.append('| style="text-align:right;" |%i' % parts[i].qty)
		lines.append('| style="text-align:right;" |$%.2f' % (parts[i].price*parts[i].qty))
	# Footer
	lines.append('|}')
	for line in lines: print(line)
	total = sum(x.qty*x.price for x in parts)
	print('Total Misumi cost: $%.2f' % total)

def generateOpenBuildsBom():
	supplier = 'OpenBuilds'
	parts = [x for x in bom if x.identifier==supplier]
	lines = ["'Part'\tQty\tURL"]
	for i in range(len(parts)):
		lines.append("'%s'\tx%s\t%s" % (parts[i].desc, parts[i].qty, parts[i].url))
	for line in lines:
		print(line)

# For RepRap wiki table
def generateNonMisumiWikiTable():
	suppliers = ['OpenBuilds', 'RepRap Discount', 'E3D']
	for s in suppliers:
		lines = []
		parts = [x for x in bom if x.identifier==s]
		# Header
		lines.append('')
		lines.append('====%s====' % s)
		lines.append('{| class="wikitable"')
		lines.append('! Description')
		lines.append('! Quantity')
		lines.append('! Unit Cost (USD)')
		lines.append('! Total (USD)')
		# Add entry for each part
		for i in range(len(parts)):
			lines.append('|-')
			lines.append('|[%s %s]' % (parts[i].url, parts[i].desc))
			lines.append('| style="text-align:right;" | %i' % parts[i].qty)
			lines.append('| style="text-align:right;" |$%.2f' % (parts[i].price*parts[i].qty))
		# Footer
		lines.append('|}')
		for line in lines: print(line)
		total = sum(x.qty*x.price for x in parts)
		print('Total %s cost: $%.2f' % (s, total))

def printAll():
	print ('Description\tQty\tUnitPrice\tTotal')
	for x in bom:
		print ("'%s'\t%i\t$%.2f\t%.2f'" % (x.desc, x.qty, x.price, x.price*x.qty))
	print ('Total cost: %.2f' % sum(x.qty*x.price for x in bom))




#printPrintable()
#print('')
#generateMisumiBOM()
#print ''
generateMisumiWikiTable()
#generateNonMisumiWikiTable()
#generateMisumiBOM()
#generateOpenBuildsBom()
#printAll()
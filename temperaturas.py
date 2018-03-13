from lxml import etree
import sys
raiz=etree.parse('sevilla.xml')

def obtener_id_municipio(municipio):
	id = raiz.xpath('//provincia/municipio[text()="{}"]/@value'.format(municipio))
	if id != []:
		id = id[0][-5:]
		return id
	print('El municipio no existe')
	sys.exit()

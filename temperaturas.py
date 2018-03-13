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

def temperaturas(municipio):
	url = etree.parse('http://www.aemet.es/xml/municipios/localidad_'+obtener_id_municipio(municipio)+'.xml')
	maxi = url.xpath("//temperatura/maxima/text()")[0]
	mini = url.xpath("//temperatura/minima/text()")[0]
	print(municipio,maxi,mini)

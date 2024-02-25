# Write your code here :-)
import pyqrcode
url=pyqrcode.create("www.seyontax.ca")
url.svg("SeyonTax.svg", scale=10)

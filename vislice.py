import bottle
import model

vislice = model.Vislice()

@bottle.get("/")  
def index():
    return bottle.template('index.tpl')

@bottle.get("/igra/") 
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre)) 

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('igra.tpl', id_igre=id_igre, igra=igra, poskus=poskus)

bottle.run(reloader=True, debug=True)
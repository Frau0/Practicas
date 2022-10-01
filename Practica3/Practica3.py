import requests
url="https://pokeapi.co/api/v2/evolution-chain"
res=requests.get(url) #peticion 1
if res.status_code==200:
    jsonlist=res.json()
    cont=1
    for cad in jsonlist['results']:
        urldecad=cad['url']
        print("La url de la cadena ", str(cont), "es", urldecad)
        rescad=requests.get(urldecad) #peticion 2 dependiente de la anterior
        jsoncad=rescad.json()
        poke1=jsoncad['chain']['species']['name']
        poke2=jsoncad['chain']['evolves_to'][0]['species']['name']
        try:
            poke3=jsoncad['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
            print("Los pokemon de la cadena", str(cont), "evolutiva son", poke1, ",", poke2, "y", poke3, "\n")
        except:
            print("Los pokemon de la cadena", str(cont), "evolutiva son", poke1, "y", poke2, "\n")
        cont+=1
    print("Podemos obetener la informacion de uno de los pokemon anteriores:")
    urlpoke=jsoncad['chain']['species']['url']
    respoke=requests.get(urlpoke) #peticion 3 dependiente de la anterior
    jsonpoke=respoke.json()
    ambase=jsonpoke['base_happiness']
    print("Por ejemplo la amistad base de ", poke1, "es: ", ambase)
    urlregion="https://pokeapi.co/api/v2/generation/1"
    resreg=requests.get(urlregion) #peticion 4
    jsonreg=resreg.json()
    nomreg=jsonreg['main_region']['name']
    print("\nO informacion de regiones")
    print("La region de la primera generacion es:", nomreg)
    urlmove="https://pokeapi.co/api/v2/move/1"
    resmove=requests.get(urlmove) #peticion 5
    jsonmove=resmove.json()
    punte=jsonmove['accuracy']
    print("\nO incluso la punteria de un movimiento como pound la cual es: ", punte)

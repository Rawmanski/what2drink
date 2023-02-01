# what2drink

django app für eine cocktail suche mit Hilfe der cocktailDB API


# requirements
python 3.9.16

    certifi==2022.12.7
    charset-normalizer==3.0.1
    Django==4.1.5
    idna==3.4
    requests==2.28.2
    sqlparse==0.4.3
    urllib3==1.26.14

die requirements mit pip installieren, dazu im Terminal folgenden Befehl im projekt Ordner ausführen
    pip install -r requirements

# API und Andpoint

Die Suche erfolgt mittels der *cocktailDB API*, die unter 
> https://www.thecocktaildb.com/api.php

erreichbar ist.

Es wird der endpoint für *die Suche nach dem Namen* der Cocktails genutzt
> https://www.thecocktaildb.com/api/json/v1/1/search.php?s=

am Ende kommt der parameter, z.B. für Margarita 
> https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita





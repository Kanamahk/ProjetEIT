
eit : avancer => attention : soutenance semaine du 15/01 + rapport sous forme de carnet de recherche

carnet de recherche : lister ce qui a ete fait, pk, les resultat / rapport resultat attendu, expliquer pk



to do :
	traitement : fautes, normalisation, 
	
parsing des fichiers de resultats wapiti pour faire des stats	

carnet de recherche : regarder les impacts des ngrams (de mots et de lettres)


creer les fichiers d'entrainements et d'avaluation : 
	a partir du fichier "../CLEFeHealth2017Task1_training_FR1/corpus/train/AlignedCauses_2006-2012full.csv"
	prendre n de tail pour l'un et n+1 de head pour l'autre (penser à retirer la premiere ligne qui ne sert a rien)

	n peut etre de l'ordre de 10 000 pour des tests rapide (moins pour etre plus rapide)
	et de l'orde des 100 000 pour faire de bonne evaluation
	
	Ces fichiers ne doivent absolument pas etre push sur github

commande pour faire tourner notre programme
	python3 main.py 
					-s "modelName" //sauvegarder le model
					-m "model" // utiliser un model existant
					-t pathToTrainFile ("../CLEFeHealth2017Task1_training_FR1/corpus/train/train.csv" par defaut)
					-e pathToEvalFile ("../CLEFeHealth2017Task1_training_FR1/corpus/train/train.csv" par defaut)
					-ngramW NumberOfWord (optional; default is 1)
					-ngramC NumberOfChar (optional)
					
	les fichiers creer ne doivent absolument pas etre push sur github

commandes wapiti
	commande pour entrainer le modele
	../wapiti-1.5.0/wapiti train --me -a rprop -d evalData -1 0.5 trainData model

	differentes commandes pour evaluer le modele et recuperation des log avec pipe
	../wapiti-1.5.0/wapiti label --me -m model evalData | head

	../wapiti-1.5.0/wapiti label --me -m model evalData /dev/null -c

	../wapiti-1.5.0/wapiti label --me -m model evalData -s | head

	../wapiti-1.5.0/wapiti label --me -m model evalData -p -s -n 3 | less  (on recupere les 3 premiers guess)
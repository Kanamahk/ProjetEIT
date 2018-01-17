
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
					-dico
					-p
					
	les fichiers creer ne doivent absolument pas etre push sur github
	
	python3 main.py -t "..\CLEFeHealth2017Task1_training_FR1\corpus\train\train.csv" -e "..\CLEFeHealth2017Task1_training_FR1\corpus\train\eval.csv" -s "modelUcode" -ngramW 3 -dico -p

commandes wapiti
	commande pour entrainer le modele
	../wapiti-1.5.0/wapiti train --me -a rprop -1 0.5 trainData.passurgit model

	differentes commandes pour evaluer le modele et recuperation des log avec pipe
	../wapiti-1.5.0/wapiti label --me -m model evalData.passurgit -c > machine-labeled

	../wapiti-1.5.0/wapiti label --me -m model evalData.passurgit -c -n 3 > machine-labeled  (on recupere les 3 premiers guess)
	
commande pour calculer taux erreur, precision, rappel
	python3 parseResults.py evalData.passurgit machine-labeled
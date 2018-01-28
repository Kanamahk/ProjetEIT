#bash classique
python3 main.py -t "../CLEFeHealth2017Task1_training_FR1/corpus/train/train100000.csv" -e "../CLEFeHealth2017Task1_training_FR1/corpus/train/eval.csv" -esc -dico substitutionTable -s modelFinal -ngramC 4 -ngramW 4 -p
../wapiti-1.5.0/wapiti train --me -a rprop -i 100 -1 0.5 trainData.passurgit model_1
../wapiti-1.5.0/wapiti label --me -m model_1 evalData.passurgit -c > machine-labeled_1
python3 parseResults.py evalData.passurgit machine-labeled_1 "data 1:" 
# bash final
python3 main.py -t "../CLEFeHealth2017Task1_training_FR1/corpus/train/train100000.csv" -e "../CLEFeHealth2017Task1_Test_FR1/corpus/AlignedCauses_2014test.csv" -esc -dico substitutionTable -s modelFinal -ngramC 4 -ngramW 4 -p
../wapiti-1.5.0/wapiti train --me -a rprop -1 0.5 trainData.passurgit modelFinal
../wapiti-1.5.0/wapiti label --me -m modelFinal evalData.passurgit -c > machine-labeled_Final
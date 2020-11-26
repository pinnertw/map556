yVal=0
dataLine=1
for i in {1..100}
do
    echo "$i"
    python3 controle_etudiant.py --vent ../data/vent_$i.csv
    xVal=$(awk -v dataLine="$dataLine" 'NR==dataLine{print $0}' mon_resultat.txt)
    yVal=$(echo $yVal+$xVal | bc)
done
(echo $yVal/100 | bc) > estimation.txt

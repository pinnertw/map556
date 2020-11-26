for i in Tristan Ancel Noble Delaunay Miras Mirone Ming Ming2 Peng-Wei $1
do
    cp Fonction_A_Tester.py $i
    cp test.sh $i
done

for i in Tristan Ancel Noble Delaunay Miras Mirone Ming Ming2 Peng-Wei $1
do
    cd $i
    sh test.sh
    cd ../
done

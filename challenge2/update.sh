for i in base jules max4 tristan pengwei
do
    echo $i
    cp test.py $i
    cp Angrybird.py $i
    cd $i
    python3 test.py
    cd ..
done

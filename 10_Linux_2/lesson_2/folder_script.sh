for file in {1..10}
do 
	touch test$file 
done
for file in $(ls)
	do
	cp $file $file.bak
done


for cate in `ls`
do
	if [[ $cate == "a"* ]]
	then
		cd $cate
		for file in `ls`
		do
			if [[ $file == *"tion"* ]]
			then
				rm -f $file
			fi
		done
		cd ..
	fi
done

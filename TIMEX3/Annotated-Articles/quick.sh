for file in *.txt
do
  cp "$file" "${file/.txt/.ann}"
done

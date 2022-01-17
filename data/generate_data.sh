ls start | sed 's/$/ 1/' > data.txt
ls end | sed 's/$/ 2/' >> data.txt
ls battle | sed 's/$/ 0/' >> data.txt



#PASSWORDUSER=$1
#if [ -d hello-world ]; then
#	rm -rf hello-world
#fi

#git clone https://pedrillogdl:$PASSWORDUSER@github.com/pedrillogdl/hello-world.git

cd hello-world/Lab6.1
prospector > ReportProspector.txt
echo "This is the report for executing prospector(same content can be found in ReportProspector.txt)	:"
cat ReportProspector.txt
git add ReportProspector.txt
git commit -m "Creating ReportProspector.txt file"
git push origin


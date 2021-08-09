Just an attempt which saves us from the annoying task of verifying Nessus SSL & SSH issues with Nmap NSE scripts.
Note that the screenshot business has to be done manually.

What’s automated?       
The manual process of giving the Nmap Script commands for all affected Hosts and ports with suitable NSE scripts. The script covers almost every SSH & SSL issues given by Nessus. 

How the script works?   
It compares the provided Nessus CSV file, having all the issues with affected hosts and ports, against the entries in scripts.csv file (repository of issues & respective NSE scripts) and run the Nmap scripts for each.

Usage:
1.	Export the VAPT report from Nessus in CSV format and save it to the directory where the script resides.

2.	Use the command: python NmapNessus.py <Nessus_CSV_File>

You can always add new findings to the repository, scripts.csv, in case of issues missed out.


# -*- coding: utf-8 -*-
"""
Title: Web application to retrieve BLAST results for a FASTA sequence

Date: 10-03-2021
Author: Meghana Balasubramanian

"""
# importing Flask and other modules 
from flask import Flask, request, render_template  
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline, NcbiblastpCommandline, NcbiblastnCommandline, NcbitblastxCommandline, NcbitblastnCommandline


# Flask constructor 
app = Flask(__name__)    
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/', methods =["GET", "POST"]) 
def gfg(): 
    if request.method == "POST": 
        # getting input with name = seq in HTML form 
        
        ip_sequence = request.form.get("seq")
        ip_type = request.form.get("ip_type")
        blast_type = request.form.get("blast_type")
        database_type = request.form.get("database")
        my_blast_db = request.form.get("db_typeo")
        e_value_thresh = request.form.get("evalue")
        e_value_thresh = float(e_value_thresh)
        
        #default e-value
        if e_value_thresh=="":
            e_value_thresh=0.05
        
    
        if ip_type =="fastq":
            seq_id = ip_sequence.split("\n")[0] #sequence id only
            seq_fasta = "".join(ip_sequence.split("\n")[1]) #gives only sequence
            
            fasta_seq= seq_id + "\n" + seq_fasta
            
        elif ip_type =="fasta":
            seq_id = ip_sequence.split("\n")[0]
            seq_fasta = ip_sequence.split("\n")[1]
            fasta_seq= "\n".join(ip_sequence.split("\n")[1:])
            
        if my_blast_db=="":
            print("1")
            #blast over internet
            result_handle=NCBIWWW.qblast(blast_type, database_type, fasta_seq)
            with open("outputhtml.xml", "w") as save_to:
                save_to.write(result_handle.read())
                result_handle.close()
        else:
            #local blast
            #if loop for each blast type:
            if blast_type=="blastn":
                result_handle=NcbiblastnCommandline(cmd=blast_type, query=fasta_seq, db=my_blast_db, evalue=e_value_thresh, out="outputhtml.xml")
            elif blast_type=="blastp":
                result_handle=NcbiblastpCommandline(cmd=blast_type, query=fasta_seq, db=my_blast_db, evalue=e_value_thresh, out="outputhtml.xml")
            elif blast_type=="blastx":
                result_handle=NcbiblastxCommandline(cmd=blast_type, query=fasta_seq, db=my_blast_db, evalue=e_value_thresh, out="outputhtml.xml")
            elif blast_type=="tblastx":
                result_handle=NcbitblastxCommandline(cmd=blast_type, query=fasta_seq, db=my_blast_db, evalue=e_value_thresh, out="outputhtml.xml")
            elif blast_type=="tblastn":
                result_handle=NcbitblastnCommandline(cmd=blast_type, query=fasta_seq, db=my_blast_db, evalue=e_value_thresh, out="outputhtml.xml")
        #blast parsing
        blast_records = NCBIXML.parse(result_handle)
        
        with open("outputhtml.xml") as f:
            blast_records = NCBIXML.parse(f)
            blast_record = list(blast_records)[0]
        
        return render_template("output.html", 
                                blast_record=blast_record, 
                                e_value_threshold=e_value_thresh)
    
    return render_template("input.html") 
  
if __name__=='__main__': 
   app.run(debug=True) 
   
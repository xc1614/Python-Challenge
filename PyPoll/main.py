import os
import csv
election_path=os.path.join("Resource","election_data.csv")
Candidate_name=''
totalVotes=0
Candidates=[]
all_Candidates={}
Winning_Candidate=''
winning_count=0


with open(election_path) as csv_file:
    csvreader= csv.reader(csv_file, delimiter=",")
    csv_header=next(csvreader)
    
    totalVotes=totalVotes+1
    
    for row in csvreader:
        totalVotes=totalVotes+1
        
        Candidate_name=row[2] 
        if Candidate_name not in Candidates:
            Candidates.append(Candidate_name)
            all_Candidates[Candidate_name]=0
        all_Candidates[Candidate_name]+=1
        
    with open ("Analysis/txt_file.write", "w")as txt_file:
        
        for candidate in all_Candidates:
            Vote_number=all_Candidates.get(candidate)
            Pecentage=Vote_number/totalVotes

            if Vote_number>winning_count:
                winning_count=Vote_number
                Winning_Candidate=candidate
                

            txt_file.write("Election Results")
            txt_file.write('\n')
            txt_file.write(".............................")
            txt_file.write('\n')
            txt_file.write("total vote:"+str(totalVotes))
            txt_file.write('\n')
            txt_file.write(".............................")
            txt_file.write('\n')
            

            for candidate, Vote_number in all_Candidates.items():
                txt_file.write(candidate+":"+"{:.3%}".format(Vote_number/totalVotes)+"("+str(Vote_number)+")")
                txt_file.write('\n')
            
            txt_file.write(".............................")
            txt_file.write('\n')
            txt_file.write("winner:"+Winning_Candidate)
            txt_file.write('\n')




 
           
                

       
      
            
    

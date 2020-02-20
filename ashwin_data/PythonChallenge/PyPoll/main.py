import os
import csv

csvpath=os.path.join('/Users/neethaabraham/Documents/ashwin_data/election_data.csv')

votes=0
candidate_list=[]
vote_count={}
winner=0

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvfile)

    for election_data in csvreader:
        votes=votes+1
        if election_data[2] not in candidate_list:
            candidate_list.append(election_data[2])
            vote_count[election_data[2]]=0
        vote_count[election_data[2]]=vote_count[election_data[2]]+1

    for candidates in vote_count:
        candidate_vote=vote_count.get(candidates)
        percent_vote=(int(candidate_vote)/votes)*100

        if (candidate_vote>winner):
            winner=candidate_vote
            winner_name=candidates

        print(f'{candidates}: {percent_vote} {(candidate_vote)}')



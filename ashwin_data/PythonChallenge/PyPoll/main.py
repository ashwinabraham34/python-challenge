import os
import csv

csvpath=os.path.join('/Users/neethaabraham/Documents/ashwin_data/election_data.csv')
output_path=os.path.join('/Users/neethaabraham/Documents/ashwin_data/PythonChallenge/PyPoll/PyPoll_Result.txt')

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
    print(
        f'Election results\n'
        f'______________________\n'
        f'Total Votes: {votes}\n'
        f'______________________\n'
    )
with open(output_path,'w',newline='') as text:

    text.write(
            f'Election results\n'
            f'______________________\n'
            f'Total Votes: {votes}\n'
            f'______________________\n')

    for candidates in vote_count:
        candidate_vote=vote_count.get(candidates)
        percent_vote=(int(candidate_vote)/votes)*100
        percent_vote=round(percent_vote,4)

        if (candidate_vote>winner):
            winner=candidate_vote
            winner_name=candidates

        winner_result=(
        f'_______________________\n'
        f'winner: {winner_name}')

        print(f'{candidates}: {percent_vote}% ({candidate_vote})')   

        text.write(f'{candidates}: {percent_vote}% ({candidate_vote})\n')
    text.write(winner_result)
print(winner_result)


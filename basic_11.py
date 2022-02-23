import numpy as np; import pandas as pd
import json
pd.options.display.max_rows = 10
class practice:
   
    def movielens():
        unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
        users = pd.read_table('C:\\Users\\kjsj9\\Desktop\\pydata-book-2nd-edition\\pydata-book-2nd-edition\\datasets\\movielens\\users.dat',
                              sep = '::',
                            header = None, names = unames)
        
        rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        ratings = pd.read_table('C:\\Users\\kjsj9\\Desktop\\pydata-book-2nd-edition\\pydata-book-2nd-edition\\datasets\\movielens\\ratings.dat',
                                sep = '::',
                            header = None, names = rnames)
            
        mnames = ['move_id', 'title', 'genres']
        movies = pd.read_table('C:\\Users\\kjsj9\\Desktop\\pydata-book-2nd-edition\\pydata-book-2nd-edition\\datasets\\movielens\\movies.dat',
                            sep = '::',
                            header = None, names = mnames)

        #print("\nfive users:\n", users[:5])
        #print("\nfive ratings:\n", ratings[:5])
        #print("\nfive movies:\n", movies[:5])
        
        print("\nratings:\n", ratings)
        print(movies)
        print(users)
        
        
        
        
        data = pd.merge(pd.merge(ratings, users, how = 'outer'), movies, how = 'outer')
        print("\nmerged data:\n", data)
        
        print("\nfirst user:\n", data.iloc[0])
        
        mean_ratings = data.pivot_table('rating', index = 'title',
                                        columns = 'gender', aggfunc = 'mean')
        print("\nmean ratings by gender of movies:\n", mean_ratings[:6])
        
        ratings_by_title = data.groupby('title').size()
        print(ratings_by_title[:10])
        
        active_titles = ratings_by_title.index[ratings_by_title >= 250]
        print("\nactive titles:\n", active_titles)
    
        top_f_ratings = mean_ratings.sort_values(by = 'F', ascending = False)
        print("\n top 10 female top ratings:\n", top_f_ratings[:10])
        
        
        
        
        mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
        
        sorted_by_diff = mean_ratings.sort_values(by = 'diff')
        
        print("\npreferred by female to male:\n", sorted_by_diff)
        
        
        
        
    def vote():
        fec = pd.read_csv('C:\\Users\\kjsj9\\Desktop\\pydata-book-2nd-edition\\pydata-book-2nd-edition\\datasets\\fec\\P00000001-ALL.csv')
        print("\nfec info:\n", fec.info())
        
        print("\n123456th fec:\n", fec.iloc[123456])
        
        unique_cands = fec.cand_nm.unique()
        
        parties = {'Bachmann, Michelle' : 'Republican',
                 'Cain, Herman' : 'Republican',
                 'Gingrich, Newt' : 'Republican',
                 'Huntsman, Jon' : 'Republican',
                 'Johnson, Gary Earl' : 'Republican',
                 'McCotter, Thaddeus G' : 'Republican',
                 'Obama, Barack' : 'Democrat',
                 'Paul, Ron' : 'Republican',
                 'Pawlenty, Timothy' : 'Republican',
                 'Perry, Rick' : 'Republican',
                 "Roemer, Charles E. 'Buddy' III" : 'Republican',
                 'Romney, Mitt' : 'Republican',
                 'Santorum, Rick' : 'Republican'}
        
        print("\ncandidate 123456 to 123461:\n", fec.cand_nm[123456:123461])
        
        fec['party'] = fec.cand_nm.map(parties)
        
        print("\nparty counts:\n", fec['party'].value_counts())
        
        print(("give or return:\n", (fec.contb_receipt_amt > 0).value_counts()))
        
        fec = fec[fec.contb_receipt_amt > 0]
        
        fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
        
        print("\n 10 occupations: \n", fec.contbr_occupation.value_counts()[:10])
       
        by_occupation = fec.pivot_table('contb_receipt_amt',
                                        index ='contbr_occupation',
                                        columns = 'party', aggfunc = 'sum')
        over_2mm = by_occupation[by_occupation.sum(1) > 2000000]
        
        print("\nover 2mil:\n", over_2mm)
        
        print(over_2mm.plot(kind = 'barh'))
        
        

                
        
        
    if __name__ == "__main__":
        #movielens()
        vote()
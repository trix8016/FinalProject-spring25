# Chapter 1 Lab Report: Search Algorithms
## Student Information
- Name: Mario De La Cruz Lujan
- Date: 01/21/2025
## Implementation Overview
[ Linear search and binary search]
## Test Results
[got 0.00? data set small ]
## Challenges and Solutions
[Binary search failed because of mixed data types fixed by str()]
## Learning Outcomes
[More debugging and practical insight]
 # Chapter 2 Lab Report: Sorting Algorithms
 ## Implementation Overview
[I wrote a selection sort to sort books by rating. It finds the smallest rating and swaps it to the front over and over.]

 ## Test Results
 [Books showed up in a random order at first. After sorting they were in order from lowest to highest rating. Sorting was kind of slow but worked. I also double checked work]

 ## Challenges and Solutions
 [Some books had no rating. That broke the code, so I gave them a rating of 0.0.]

 ## Learning Outcomes
 [I learned how selection sort works and how to load and sort data from a file. It’s not the fastest way to sort, but it’s simple.]
 # Chapter 3 Lab Report: Merge Sort

 ## Implementation Overview
 [ added merge sort so it can sort books by rating. It splits the list in half a bunch of times and then puts it back together in order.]

 ## Test Results
[ before sorting the books were all over the place. After merge sort, they were sorted from lowest to highest rating It was faster than selection sort]

 ## Challenges and Solutions
 [ messed up the merge function at first and got weird results. Fixed it by comparing the ratings correctly while merging.]

 ## Learning Outcomes
[ Merge sort is better than selection sort for big lists. I learned how to use recursion and how to not break stuff when copying lists.]

# chapter 4 lab report quick sort

## implementation overview
[ made quick sort to sort books by rating it picks a pivot and moves stuff around then does it again]

## test results
[books were random at first after quick sort they were in order by rating it was fast like merge sort the lowest and highest rated books were correct]

## challenges and solutions
[partition was confusing i swapped the wrong books a few times fixed it by printing stuff to see what was going on]

## learning outcomes
[quick sort is fast and uses recursion i learned how to split up a list and put it back without messing up the ratings]

# chapter 5 lab report hash tables and enhanced data structures


## implementation overview  
[i created a hash table using a python dictionary  
i added insert get and delete functions  
i used book titles as keys and ratings as values  ]

## test results  
[i tested looking up the rating for the book matilda  
the lookup was fast and successful  
i deleted matilda and confirmed it was gone from the table  
the search and delete times were printed  ]

## challenges and solutions  
[i had an error because the hash table code was outside the main function  
i moved the code inside main and it worked] 

## learning outcomes  
[i learned how hash tables store key value pairs  
i learned that hash tables are fast for lookups  
i practiced writing modular code and measuring performance]

# chapter 6 lab report breadth first search and graphs

## implementation overview  
[i created a graph from the books using shared authors  
i used a dictionary where each book connects to others by the same author  
i implemented breadth first search to look for a path between two books] 

## test results  
[i searched for a path from les misérables to the hunchback of notre dame  
the program visited books using bfs and found the connection  
output showed visited nodes and confirmed the path]  

## challenges and solutions  
[some books were missing author info so they were skipped  
i added checks to make sure only books with authors were processed] 

## learning outcomes  
[i learned how to build graphs 
i also got better at using dictionaries and loops in python]

# chapter 7 lab report depth first search algorithm

## implementation overview  
[i made a dfs function that uses recursion  
it goes from one book to another through shared authors  
i used the same graph from chapter 6 to keep it simple ]

## test results  
[i searched from les misérables to the hunchback of notre dame  
dfs visited both nodes and said the path was found  
output showed which books it visited step by step]

## challenges and solutions  
[at first i put the code outside the main function and it broke  
i moved it inside main and it worked fine]

## learning outcomes  
[i learned how dfs explores deep before it backtracks  
 saw how it can find paths in graphs like bfs but in a different way  
 practiced using recursion and sets to track visited books]

# chapter 8 lab report avl tree algorithm

## implementation overview  
[i made a class for avl tree with insert and rotation methods  
the tree balances itself when adding books based on rating  
 used inorder traversal to get a sorted list of books]  

## test results  
[i used a few books and added them into the avl tree  
the traversal printed them from lowest to highest rating  
the tree stayed balanced and worked like expected ]

## challenges and solutions  
[i forgot to add the insert_book method at first  
after adding it to the class it fixed the error] 

## learning outcomes  
[learned how avl trees stay balanced using rotations  
 saw how recursion and height checks help with structure  
and now know how to build and walk through a tree in python ]

# chapter 9 lab report dijkstra's algorithm

## implementation overview  
[i created a graph where books are nodes and edges are based on rating difference also used dijkstra's algorithm to find the shortest path between two books and it picks the path with the smallest total rating difference using a heap] 

## test results  
[i tested the path between bridge to terabithia and charlotte's web  
the program found a valid path and showed both books and the total path weight was 0.50 which means their ratings are very close]  

## challenges and solutions  
[i had to make sure ratings were converted to floats  
and also had to check that the graph only connects similar rated books] 

## learning outcomes  
[i learned how dijkstra’s algorithm works with priority queues  
also saw how it finds the best route between nodes in a graph  
amd i practiced building weighted graphs from real data] 

# chapter 10 lab report greedy algorithm

## implementation overview  
[i used a greedy algorithm to cover a list of target authors  
the code picks the book that covers the most new authors until all are covered  
each book was checked based on the authors in it]

## test results  
[i searched for five authors  
the program picked five different books that matched them  
the output showed each selected book and author]  

## challenges and solutions  
[code was in wrong area moved to correct spot]  

## learning outcomes  
[i learned how greedy algorithms work by picking the best option at each step  
i saw how to apply it to book data and authors  
i practiced working with sets and loops to solve real problems ] 

# chapter 11 lab report dynamic programming

## overview  
[i used levenshtein distance to compare book titles  
it finds how many edits are needed to turn one title into another  
i picked the pair with the lowest normalized distance]  

## result  
[it found 'holes' and 'charlotte's web' were the closest match  
distance was 0.73 and a small part of the dp matrix was shown]  

## what i learned  
[i learned how to use a matrix to track string changes  
this helped find text similarity in a smart way]  
# chapter 12 lab report knn algorithm

## overview  
[i used cosine similarity to compare books  
each book was represented by rating and page count  
the algorithm picked the top 5 most similar books] 

## result  
[bridge to terabithia was the target  
it found five others with the same similarity score  
they all had very close rating and page data]  

## what i learned  
[i learned how to use vectors and cosine similarity  
it was useful to measure closeness between books]  


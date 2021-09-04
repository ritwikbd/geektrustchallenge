# geektrustchallenge
Coding Challenge for GeekTrust

<h1> Approach </h1>
  The approach from the very beginning has been a procedural one. As mentioned in the challenge, this is to be run once for every investor. Hence, we do not need multiple objects for this, so a procedural method has been taken.
  There is a file named database.txt that mimics the way Redis works through the functions written around it. All monthly values are stored in the same
  This can be scaled up by using a randomised portfolio id for all multiple users and creating a fully running DB. The effort has been mainly around the scalability of the project.
 <h1> Execution </h1>
 
  No build script is provided. Complex build scripts may hurt the scalability of the project. Just 2 commands will be enough:
  
  `pip install -r requirements.txt`
  
  `python -m geektrust <absolute_path_to_input_file>`
          
 <h1> Scalability Provisions </h1>
 
 The following items have been incorporated for improving scalability of the project:
 
 1.  Redis like database concept: The database.txt file can be easily replaced with a database that can provide values associated with a key or fabricate queries based on commands. The scalability extends to both SQL and NoSQL type of databases.
 2.  Exit codes for all commands. The exit codes are spceifically present for making debugging much easier
 3.  The inclusion of pandas library can be precursor to some data munging that can be done later to recommend good investments or predict returns

<h1> Further Items </h1>

The code does not have any provision for multiple years with repition of months. This was not properly defined in the problem statement and no sample inputs for such a case was given.

Assumptions given in the problem statement have been taken into account.
